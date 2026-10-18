# bi_windup

- RVA: `0x00600F50`–`0x00600FA8` (길이 `88` bytes)
- VA: `0x0000000140600F50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `23`개 명령, `88/88` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [tr_flush_block](tr_flush_block_function_00600AF8.md) at `0x00600D96`
- [tr_stored_block](tr_stored_block_function_00600DC0.md) at `0x00600E4F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00600F50  8B 81 60 17 00 00               mov eax, dword ptr [rcx + 0x1760]
00600F56  45 33 D2                        xor r10d, r10d
00600F59  4C 8B C9                        mov r9, rcx
00600F5C  83 F8 08                        cmp eax, 8
00600F5F  7E 1D                           jle 0x140600f7e
00600F61  44 8B 41 28                     mov r8d, dword ptr [rcx + 0x28]
00600F65  8A 81 5C 17 00 00               mov al, byte ptr [rcx + 0x175c]
00600F6B  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
00600F6F  41 88 04 10                     mov byte ptr [r8 + rdx], al
00600F73  FF 41 28                        inc dword ptr [rcx + 0x28]
00600F76  8A 81 5D 17 00 00               mov al, byte ptr [rcx + 0x175d]
00600F7C  EB 0B                           jmp 0x140600f89
00600F7E  85 C0                           test eax, eax
00600F80  7E 15                           jle 0x140600f97
00600F82  41 8A 81 5C 17 00 00            mov al, byte ptr [r9 + 0x175c]
00600F89  8B 51 28                        mov edx, dword ptr [rcx + 0x28]
00600F8C  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00600F90  88 04 0A                        mov byte ptr [rdx + rcx], al
00600F93  41 FF 41 28                     inc dword ptr [r9 + 0x28]
00600F97  66 45 89 91 5C 17 00 00         mov word ptr [r9 + 0x175c], r10w
00600F9F  45 89 91 60 17 00 00            mov dword ptr [r9 + 0x1760], r10d
00600FA6  C3                              ret
00600FA7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall bi_windup(__int64 a1)
{
    __int64 v_r10;

    v_r10 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 5984)))) <= 8) goto loc_00600F7E;
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 40)) + *(unsigned __int64 *)(a1 + 16) * 1) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 5980));
    goto loc_00600F89;
loc_00600F7E:
    if (condition_is_less_or_equal) goto loc_00600F97;
loc_00600F89:
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 40)) + *(unsigned __int64 *)(a1 + 16) * 1) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 5980));
loc_00600F97:
    *(unsigned __int16 *)(a1 + 5980) = 0;
    *(unsigned int *)(a1 + 5984) = 0;
    return *(unsigned __int8 *)(a1 + 5980);
}
```

## 5. (Beta) C Style

```c
int64_t bi_windup(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_r10;

    local_r10 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1760)))) <= 8) goto loc_00600F7E;
    *(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x28)) + *(uint64_t *)(arg1 + 0x10) * 1) = (uint8_t)(*(uint8_t *)(arg1 + 0x175C));
    goto loc_00600F89;
loc_00600F7E:
    if (condition_is_less_or_equal) goto loc_00600F97;
loc_00600F89:
    *(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x28)) + *(uint64_t *)(arg1 + 0x10) * 1) = (uint8_t)(*(uint8_t *)(arg1 + 0x175C));
loc_00600F97:
    *(uint16_t *)(arg1 + 0x175C) = 0;
    *(uint32_t *)(arg1 + 0x1760) = 0;
    return *(uint8_t *)(arg1 + 0x175C);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R/W` |
| `Arg1` | `+ 0x175C` | `8` | `R` |
| `Arg1` | `+ 0x175C` | `16` | `W` |
| `Arg1` | `+ 0x175D` | `8` | `R` |
| `Arg1` | `+ 0x1760` | `32` | `R` |
| `Arg1` | `+ 0x1760` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00600F50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00600F50[BB_00600F50]
  bb_00600F61[BB_00600F61]
  bb_00600F7E[BB_00600F7E]
  bb_00600F82[BB_00600F82]
  bb_00600F89[BB_00600F89]
  bb_00600F97[BB_00600F97]
  bb_00600FA7[BB_00600FA7]
  bb_00600F50 -->|branch| bb_00600F7E
  bb_00600F50 -->|fallthrough| bb_00600F61
  bb_00600F61 -->|branch| bb_00600F89
  bb_00600F7E -->|branch| bb_00600F97
  bb_00600F7E -->|fallthrough| bb_00600F82
  bb_00600F82 -->|flow| bb_00600F89
  bb_00600F89 -->|flow| bb_00600F97
```
