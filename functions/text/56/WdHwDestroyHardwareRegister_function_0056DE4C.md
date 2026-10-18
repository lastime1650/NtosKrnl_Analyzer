# WdHwDestroyHardwareRegister

- RVA: `0x0056DE4C`–`0x0056DE8B` (길이 `63` bytes)
- VA: `0x000000014056DE4C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `20`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0056DE6F` → [HalpUnmapVirtualAddress](../3F/HalpUnmapVirtualAddress_function_003F8C30.md) (function, `0x003F8C30`)

### Direct callers
- [HalpWdatProcessWdrtInternalData](HalpWdatProcessWdrtInternalData_function_00560FC0.md) at `0x00561066`
- [WdInstrDestroyInstruction](WdInstrDestroyInstruction_function_0056DF14.md) at `0x0056DF21`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056DE4C  40 53                           push rbx
0056DE4E  48 83 EC 20                     sub rsp, 0x20
0056DE52  80 79 08 00                     cmp byte ptr [rcx + 8], 0
0056DE56  48 8B D9                        mov rbx, rcx
0056DE59  75 19                           jne 0x14056de74
0056DE5B  0F B6 51 09                     movzx edx, byte ptr [rcx + 9]
0056DE5F  45 33 C0                        xor r8d, r8d
0056DE62  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0056DE66  81 C2 FF 0F 00 00               add edx, 0xfff
0056DE6C  C1 EA 0C                        shr edx, 0xc
0056DE6F  E8 BC AD E8 FF                  call 0x1403f8c30
0056DE74  0F 57 C0                        xorps xmm0, xmm0
0056DE77  33 C0                           xor eax, eax
0056DE79  0F 11 03                        movups xmmword ptr [rbx], xmm0
0056DE7C  0F 11 43 10                     movups xmmword ptr [rbx + 0x10], xmm0
0056DE80  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
0056DE84  48 83 C4 20                     add rsp, 0x20
0056DE88  5B                              pop rbx
0056DE89  C3                              ret
0056DE8A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WdHwDestroyHardwareRegister(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int8 *)(a1 + 8)) == 0) {
        a2 = *(unsigned __int8 *)(a1 + 9);
        a3 = 0;
        a1 = *(unsigned __int64 *)(a1 + 16);
        a2 = (unsigned int)((a2) + (0xFFFULL));
        a2 = (unsigned int)((a2) >> (12));
        result = HalpUnmapVirtualAddress(a1, a2, a3, a4);
    }
    result = 0;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm0;
    *(unsigned __int64 *)(a1 + 32) = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WdHwDestroyHardwareRegister(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint8_t *)(arg1 + 0x8)) == 0) {
        Arg2 = *(uint8_t *)(arg1 + 0x9);
        Arg3 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        Arg2 = (uint32_t)((Arg2) + (0xFFFULL));
        Arg2 = (uint32_t)((Arg2) >> (12));
        result = HalpUnmapVirtualAddress(Arg1, Arg2, Arg3, a4);
    }
    result = 0;
    *(uint64_t *)(arg1) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10) = v_xmm0;
    *(uint64_t *)(arg1 + 0x20) = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056DE4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0056DE4C[BB_0056DE4C]
  bb_0056DE5B[BB_0056DE5B]
  bb_0056DE74[BB_0056DE74]
  bb_0056DE8A[BB_0056DE8A]
  bb_0056DE4C -->|branch| bb_0056DE74
  bb_0056DE4C -->|fallthrough| bb_0056DE5B
  bb_0056DE5B -->|flow| bb_0056DE74
```
