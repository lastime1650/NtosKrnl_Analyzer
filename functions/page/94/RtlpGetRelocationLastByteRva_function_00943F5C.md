# RtlpGetRelocationLastByteRva

- RVA: `0x00943F5C`–`0x00943F8C` (길이 `48` bytes)
- VA: `0x0000000140943F5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `16`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpSortAndValidateRelocations](RtlpSortAndValidateRelocations_function_009439BC.md) at `0x00943A0A`
- [RtlpSortAndValidateRelocations](RtlpSortAndValidateRelocations_function_009439BC.md) at `0x00943A33`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00943F5C  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
00943F60  B8 04 00 00 00                  mov eax, 4
00943F65  66 83 E2 07                     and dx, 7
00943F69  66 0F 44 D0                     cmove dx, ax
00943F6D  0F B7 01                        movzx eax, word ptr [rcx]
00943F70  B9 FF 0F 00 00                  mov ecx, 0xfff
00943F75  66 23 C1                        and ax, cx
00943F78  66 FF C8                        dec ax
00943F7B  66 03 D0                        add dx, ax
00943F7E  66 3B D1                        cmp dx, cx
00943F81  73 05                           jae 0x140943f88
00943F83  0F B7 C2                        movzx eax, dx
00943F86  C3                              ret
00943F87  CC                              int3
00943F88  8B D1                           mov edx, ecx
00943F8A  EB F7                           jmp 0x140943f83
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpGetRelocationLastByteRva(__int64 a1)
{
    __int64 result;

    a2 = (unsigned __int16)((*(unsigned __int16 *)(a1 + 2)) & (7));
    if (condition_is_equal) { a2 = 4; }
    result = (unsigned __int16)((*(unsigned __int16 *)(a1)) & ((unsigned __int16)((unsigned int)(0xFFFULL))));
    result = (unsigned __int16)((result) - 1);
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)(result)));
    if (((unsigned __int16)(a2)) >= ((unsigned __int16)((unsigned int)(0xFFFULL)))) goto loc_00943F88;
loc_00943F83:
    return (unsigned __int16)(a2);
loc_00943F88:
    goto loc_00943F83;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpGetRelocationLastByteRva(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    a2 = (uint16_t)((*(uint16_t *)(arg1 + 0x2)) & (7));
    if (condition_is_equal) { a2 = 4; }
    result = (uint16_t)((*(uint16_t *)(arg1)) & ((uint16_t)((uint32_t)(0xFFFULL))));
    result = (uint16_t)((result) - 1);
    a2 = (uint16_t)((a2) + ((uint16_t)(result)));
    if (((uint16_t)(a2)) >= ((uint16_t)((uint32_t)(0xFFFULL)))) goto loc_00943F88;
loc_00943F83:
    return (uint16_t)(a2);
loc_00943F88:
    goto loc_00943F83;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00943F5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00943F5C[BB_00943F5C]
  bb_00943F83[BB_00943F83]
  bb_00943F87[BB_00943F87]
  bb_00943F88[BB_00943F88]
  bb_00943F5C -->|branch| bb_00943F88
  bb_00943F5C -->|fallthrough| bb_00943F83
  bb_00943F87 -->|flow| bb_00943F88
  bb_00943F88 -->|branch| bb_00943F83
```
