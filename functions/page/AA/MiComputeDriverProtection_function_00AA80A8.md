# MiComputeDriverProtection

- RVA: `0x00AA80A8`–`0x00AA80E2` (길이 `58` bytes)
- VA: `0x0000000140AA80A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `19`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiProtectLargeKernelHalRange](../7F/MiProtectLargeKernelHalRange_function_007F8D20.md) at `0x007F8D4A`
- [MiProtectSystemImage](MiProtectSystemImage_function_00AA7D74.md) at `0x00AA7F3F`
- [MiProtectSystemImage](MiProtectSystemImage_function_00AA7D74.md) at `0x00AA800D`
- [MiGetBootImagePageProtection](../../init/C6/MiGetBootImagePageProtection_function_00C6B784.md) at `0x00C6B7CB`
- [MiGetBootImagePageProtection](../../init/C6/MiGetBootImagePageProtection_function_00C6B784.md) at `0x00C6B800`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA80A8  8B D1                           mov edx, ecx
00AA80AA  C1 EA 1C                        shr edx, 0x1c
00AA80AD  83 E2 02                        and edx, 2
00AA80B0  44 8B C2                        mov r8d, edx
00AA80B3  41 83 C8 01                     or r8d, 1
00AA80B7  0F BA E1 1E                     bt ecx, 0x1e
00AA80BB  44 0F 43 C2                     cmovae r8d, edx
00AA80BF  85 C9                           test ecx, ecx
00AA80C1  78 11                           js 0x140aa80d4
00AA80C3  45 85 C0                        test r8d, r8d
00AA80C6  B8 18 00 00 00                  mov eax, 0x18
00AA80CB  44 0F 44 C0                     cmove r8d, eax
00AA80CF  41 8B C0                        mov eax, r8d
00AA80D2  C3                              ret
00AA80D3  CC                              int3
00AA80D4  45 0F B6 C0                     movzx r8d, r8b
00AA80D8  41 83 E0 02                     and r8d, 2
00AA80DC  41 83 C8 04                     or r8d, 4
00AA80E0  EB ED                           jmp 0x140aa80cf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiComputeDriverProtection(int a1)
{
    a2 = (unsigned int)(((unsigned int)(a1)) >> (28));
    a2 = (unsigned int)((a2) & (2));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (1));
    if (condition_is_above_or_equal) { a3 = (unsigned int)(a2); }
    if (sign_flag) goto loc_00AA80D4;
    if ((unsigned int)(a3) == 0) { a3 = 24; }
loc_00AA80CF:
    return (unsigned int)((unsigned int)(a3));
loc_00AA80D4:
    a3 = (unsigned int)(((unsigned __int8)(a3)) & (2));
    a3 = (unsigned int)((a3) | (4));
    goto loc_00AA80CF;
}
```

## 5. (Beta) C Style

```c
int64_t MiComputeDriverProtection(int32_t Arg1)
{
    a2 = (uint32_t)(((uint32_t)(Arg1)) >> (28));
    a2 = (uint32_t)((a2) & (2));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(a2))) | (1));
    if (condition_is_above_or_equal) { a3 = (uint32_t)(a2); }
    if (sign_flag) goto loc_00AA80D4;
    if ((uint32_t)(a3) == 0) { a3 = 24; }
loc_00AA80CF:
    return (uint32_t)((uint32_t)(a3));
loc_00AA80D4:
    a3 = (uint32_t)(((uint8_t)(a3)) & (2));
    a3 = (uint32_t)((a3) | (4));
    goto loc_00AA80CF;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA80A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA80A8[BB_00AA80A8]
  bb_00AA80C3[BB_00AA80C3]
  bb_00AA80CF[BB_00AA80CF]
  bb_00AA80D3[BB_00AA80D3]
  bb_00AA80D4[BB_00AA80D4]
  bb_00AA80A8 -->|branch| bb_00AA80D4
  bb_00AA80A8 -->|fallthrough| bb_00AA80C3
  bb_00AA80C3 -->|flow| bb_00AA80CF
  bb_00AA80D3 -->|flow| bb_00AA80D4
  bb_00AA80D4 -->|branch| bb_00AA80CF
```
