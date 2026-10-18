# HalpBlkApicRead

- RVA: `0x00BEB34C`–`0x00BEB38A` (길이 `62` bytes)
- VA: `0x0000000140BEB34C`
- 실행 섹션: `MINIEX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `18`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpBlkApicInitializeLocalUnit](HalpBlkApicInitializeLocalUnit_function_00BEB1F0.md) at `0x00BEB241`
- [HalpBlkApicInitializeLocalUnit](HalpBlkApicInitializeLocalUnit_function_00BEB1F0.md) at `0x00BEB2D8`
- [HalpBlkApicInitializeLocalUnit](HalpBlkApicInitializeLocalUnit_function_00BEB1F0.md) at `0x00BEB312`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BEB34C  65 48 8B 04 25 00 00 00 00      mov rax, qword ptr gs:[0]
00BEB355  80 78 29 00                     cmp byte ptr [rax + 0x29], 0
00BEB359  75 1B                           jne 0x140beb376
00BEB35B  80 78 28 00                     cmp byte ptr [rax + 0x28], 0
00BEB35F  75 15                           jne 0x140beb376
00BEB361  65 48 8B 04 25 00 00 00 00      mov rax, qword ptr gs:[0]
00BEB36A  48 63 C9                        movsxd rcx, ecx
00BEB36D  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00BEB371  8B 04 01                        mov eax, dword ptr [rcx + rax]
00BEB374  C3                              ret
00BEB375  CC                              int3
00BEB376  C1 F9 04                        sar ecx, 4
00BEB379  81 C1 00 08 00 00               add ecx, 0x800
00BEB37F  0F 32                           rdmsr
00BEB381  48 C1 E2 20                     shl rdx, 0x20
00BEB385  48 0B C2                        or rax, rdx
00BEB388  C3                              ret
00BEB389  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBlkApicRead(int a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0)) + 41)) != 0) goto loc_00BEB376;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0)) + 40)) != 0) goto loc_00BEB376;
    return (unsigned int)(*(unsigned int *)((int)(a1) + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0)) + 32) * 1));
loc_00BEB376:
    a1 = (unsigned int)(((int)(a1)) >> (4));
    a1 = (unsigned int)((a1) + (0x800ULL));
    a2 = (a2) << (32);
    result = ((unsigned int)(*(unsigned int *)((int)(a1) + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0)) + 32) * 1))) | (a2);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpBlkApicRead(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0)) + 0x29)) != 0) goto loc_00BEB376;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0)) + 0x28)) != 0) goto loc_00BEB376;
    return (uint32_t)(*(uint32_t *)((int32_t)(arg1) + *(uint64_t *)(*(uint64_t *)(gs_base + (0)) + 0x20) * 1));
loc_00BEB376:
    Arg1 = (uint32_t)(((int32_t)(Arg1)) >> (4));
    Arg1 = (uint32_t)((Arg1) + (0x800ULL));
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)(*(uint32_t *)((int32_t)(arg1) + *(uint64_t *)(*(uint64_t *)(gs_base + (0)) + 0x20) * 1))) | (Arg2);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=miniex&rva=0x00BEB34C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BEB34C[BB_00BEB34C]
  bb_00BEB35B[BB_00BEB35B]
  bb_00BEB361[BB_00BEB361]
  bb_00BEB375[BB_00BEB375]
  bb_00BEB376[BB_00BEB376]
  bb_00BEB389[BB_00BEB389]
  bb_00BEB34C -->|branch| bb_00BEB376
  bb_00BEB34C -->|fallthrough| bb_00BEB35B
  bb_00BEB35B -->|branch| bb_00BEB376
  bb_00BEB35B -->|fallthrough| bb_00BEB361
  bb_00BEB375 -->|flow| bb_00BEB376
```
