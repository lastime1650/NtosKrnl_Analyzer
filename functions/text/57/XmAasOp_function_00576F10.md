# XmAasOp

- RVA: `0x00576F10`–`0x00576F5F` (길이 `79` bytes)
- VA: `0x0000000140576F10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `28`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00576F10  44 8A 49 18                     mov r9b, byte ptr [rcx + 0x18]
00576F14  4C 8B C1                        mov r8, rcx
00576F17  41 8A C9                        mov cl, r9b
00576F1A  80 E1 0F                        and cl, 0xf
00576F1D  49 8D 50 10                     lea rdx, [r8 + 0x10]
00576F21  80 F9 09                        cmp cl, 9
00576F24  77 14                           ja 0x140576f3a
00576F26  8B 02                           mov eax, dword ptr [rdx]
00576F28  A8 10                           test al, 0x10
00576F2A  75 0E                           jne 0x140576f3a
00576F2C  83 E0 FE                        and eax, 0xfffffffe
00576F2F  41 88 48 18                     mov byte ptr [r8 + 0x18], cl
00576F33  89 02                           mov dword ptr [rdx], eax
00576F35  83 E0 EF                        and eax, 0xffffffef
00576F38  EB 21                           jmp 0x140576f5b
00576F3A  41 8D 41 FA                     lea eax, [r9 - 6]
00576F3E  B9 FF 00 00 00                  mov ecx, 0xff
00576F43  24 0F                           and al, 0xf
00576F45  41 88 40 18                     mov byte ptr [r8 + 0x18], al
00576F49  41 80 F9 06                     cmp r9b, 6
00576F4D  0F 92 C0                        setb al
00576F50  2A C8                           sub cl, al
00576F52  8B 02                           mov eax, dword ptr [rdx]
00576F54  41 00 48 19                     add byte ptr [r8 + 0x19], cl
00576F58  83 C8 11                        or eax, 0x11
00576F5B  89 02                           mov dword ptr [rdx], eax
00576F5D  C3                              ret
00576F5E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmAasOp(__int64 a1)
{
    __int64 result;

    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + 24))) & (15));
    if (((unsigned __int8)(a1)) > 9) goto loc_00576F3A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 16)))) & (16)) != 0) goto loc_00576F3A;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) & (0xFFFFFFFEULL));
    *(unsigned __int8 *)(a1 + 24) = (unsigned __int8)(a1);
    *(unsigned int *)(a1 + 16) = (unsigned int)(result);
    result = (unsigned int)((result) & (0xFFFFFFEFULL));
    goto loc_00576F5B;
loc_00576F3A:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 24) - 6) & (15));
    *(unsigned __int8 *)(a1 + 24) = (unsigned __int8)(result);
    result = (((unsigned __int8)(*(unsigned __int8 *)(a1 + 24))) < 6) ? 1 : 0;
    a1 = (unsigned __int8)((255) - ((unsigned __int8)(result)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) | (17));
loc_00576F5B:
    *(unsigned int *)(a1 + 16) = (unsigned int)(result);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t XmAasOp(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + 0x18))) & (15));
    if (((uint8_t)(Arg1)) > 9) goto loc_00576F3A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) & (16)) != 0) goto loc_00576F3A;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) & (0xFFFFFFFEULL));
    *(uint8_t *)(arg1 + 0x18) = (uint8_t)(Arg1);
    *(uint32_t *)(arg1 + 0x10) = (uint32_t)(result);
    result = (uint32_t)((result) & (0xFFFFFFEFULL));
    goto loc_00576F5B;
loc_00576F3A:
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x18) - 6) & (15));
    *(uint8_t *)(arg1 + 0x18) = (uint8_t)(result);
    result = (((uint8_t)(*(uint8_t *)(arg1 + 0x18))) < 6) ? 1 : 0;
    Arg1 = (uint8_t)((255) - ((uint8_t)(result)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) | (17));
loc_00576F5B:
    *(uint32_t *)(arg1 + 0x10) = (uint32_t)(result);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `8` | `R` |
| `Arg1` | `+ 0x18` | `8` | `W` |
| `Arg1` | `+ 0x19` | `8` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00576F10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00576F10[BB_00576F10]
  bb_00576F26[BB_00576F26]
  bb_00576F2C[BB_00576F2C]
  bb_00576F3A[BB_00576F3A]
  bb_00576F5B[BB_00576F5B]
  bb_00576F5E[BB_00576F5E]
  bb_00576F10 -->|branch| bb_00576F3A
  bb_00576F10 -->|fallthrough| bb_00576F26
  bb_00576F26 -->|branch| bb_00576F3A
  bb_00576F26 -->|fallthrough| bb_00576F2C
  bb_00576F2C -->|branch| bb_00576F5B
  bb_00576F3A -->|flow| bb_00576F5B
```
