# IoStartNextPacket

- RVA: `0x0045F8A0`–`0x0045F8DB` (길이 `59` bytes)
- VA: `0x000000014045F8A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F758`
- 디코드: `16`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0045F8C6` → [IopStartNextPacketByKeyEx](IopStartNextPacketByKeyEx_function_0045F8E4.md) (function, `0x0045F8E4`)
- `0x0045F8D4` → [IopStartNextPacket](IopStartNextPacket_function_0045F9A4.md) (function, `0x0045F9A4`)

### Direct callers
- [DifIoStartNextPacketWrapper](../62/DifIoStartNextPacketWrapper_function_0062D2C0.md) at `0x0062D397`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045F8A0  48 83 EC 28                     sub rsp, 0x28
0045F8A4  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
0045F8AB  F7 40 40 00 01 00 00            test dword ptr [rax + 0x40], 0x100
0045F8B2  74 1D                           je 0x14045f8d1
0045F8B4  F6 DA                           neg dl
0045F8B6  45 1B C0                        sbb r8d, r8d
0045F8B9  33 D2                           xor edx, edx
0045F8BB  41 81 E0 80 00 00 00            and r8d, 0x80
0045F8C2  41 83 C0 20                     add r8d, 0x20
0045F8C6  E8 19 00 00 00                  call 0x14045f8e4
0045F8CB  48 83 C4 28                     add rsp, 0x28
0045F8CF  C3                              ret
0045F8D0  CC                              int3
0045F8D1  0F B6 D2                        movzx edx, dl
0045F8D4  E8 CB 00 00 00                  call 0x14045f9a4
0045F8D9  EB F0                           jmp 0x14045f8cb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoStartNextPacket(__int64 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 64)) & (256)) == 0) goto loc_0045F8D1;
    a2 = (unsigned __int8)(-(a2));
    a2 = 0;
    a3 = (unsigned int)((a3) & (128));
    a3 = (unsigned int)((a3) + (32));
    result = IopStartNextPacketByKeyEx(a1, a2, a3, a4);
loc_0045F8CB:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0045F8D1:
    result = IopStartNextPacket(a1, 0, a3, a4);
    goto loc_0045F8CB;
}
```

## 5. (Beta) C Style

```c
int64_t IoStartNextPacket(void *Arg1, uint8_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x40)) & (256)) == 0) goto loc_0045F8D1;
    Arg2 = (uint8_t)(-(Arg2));
    Arg2 = 0;
    Arg3 = (uint32_t)((Arg3) & (128));
    Arg3 = (uint32_t)((Arg3) + (32));
    result = IopStartNextPacketByKeyEx(Arg1, Arg2, Arg3, a4);
loc_0045F8CB:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0045F8D1:
    result = IopStartNextPacket(Arg1, 0, Arg3, a4);
    goto loc_0045F8CB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x138` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045F8A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045F8A0[BB_0045F8A0]
  bb_0045F8B4[BB_0045F8B4]
  bb_0045F8CB[BB_0045F8CB]
  bb_0045F8D0[BB_0045F8D0]
  bb_0045F8D1[BB_0045F8D1]
  bb_0045F8A0 -->|branch| bb_0045F8D1
  bb_0045F8A0 -->|fallthrough| bb_0045F8B4
  bb_0045F8B4 -->|flow| bb_0045F8CB
  bb_0045F8D0 -->|flow| bb_0045F8D1
  bb_0045F8D1 -->|branch| bb_0045F8CB
```
