# IopSetCopyInformationExtension

- RVA: `0x00444EEC`–`0x00444F1D` (길이 `49` bytes)
- VA: `0x0000000140444EEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DAC8`
- 디코드: `17`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00444EFB` → [IopAllocateIrpExtension](IopAllocateIrpExtension_function_00444F30.md) (function, `0x00444F30`)

### Direct callers
- [IopAllocateAndPopulateWriteIrp](../40/IopAllocateAndPopulateWriteIrp_function_004011F4.md) at `0x004014C2`
- [IopReadFile](../../page/8A/IopReadFile_function_008AEFF0.md) at `0x008AF890`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00444EEC  40 53                           push rbx
00444EEE  48 83 EC 20                     sub rsp, 0x20
00444EF2  48 8B DA                        mov rbx, rdx
00444EF5  90                              nop
00444EF6  BA 09 00 00 00                  mov edx, 9
00444EFB  E8 30 00 00 00                  call 0x140444f30
00444F00  48 85 C0                        test rax, rax
00444F03  74 11                           je 0x140444f16
00444F05  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00444F08  F3 0F 7F 40 40                  movdqu xmmword ptr [rax + 0x40], xmm0
00444F0D  33 C0                           xor eax, eax
00444F0F  48 83 C4 20                     add rsp, 0x20
00444F13  5B                              pop rbx
00444F14  C3                              ret
00444F15  CC                              int3
00444F16  B8 9A 00 00 C0                  mov eax, 0xc000009a
00444F1B  EB F2                           jmp 0x140444f0f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopSetCopyInformationExtension(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = IopAllocateIrpExtension(a1, 9, a3, a4);
    if (result == 0) goto loc_00444F16;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    result = 0;
loc_00444F0F:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00444F16:
    goto loc_00444F0F;
}
```

## 5. (Beta) C Style

```c
int64_t IopSetCopyInformationExtension(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = IopAllocateIrpExtension(Arg1, 9, a3, a4);
    if (result == 0) goto loc_00444F16;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    result = 0;
loc_00444F0F:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00444F16:
    goto loc_00444F0F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00444EEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00444EEC[BB_00444EEC]
  bb_00444F05[BB_00444F05]
  bb_00444F0F[BB_00444F0F]
  bb_00444F15[BB_00444F15]
  bb_00444F16[BB_00444F16]
  bb_00444EEC -->|branch| bb_00444F16
  bb_00444EEC -->|fallthrough| bb_00444F05
  bb_00444F05 -->|flow| bb_00444F0F
  bb_00444F15 -->|flow| bb_00444F16
  bb_00444F16 -->|branch| bb_00444F0F
```
