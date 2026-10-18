# MiGetColorHeadBase

- RVA: `0x003BB8B0`–`0x003BB917` (길이 `103` bytes)
- VA: `0x00000001403BB8B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008CCFC`
- 디코드: `28`개 명령, `103/103` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiGetPerfectColorHeadPage](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) at `0x00289D1F`
- [MiReplenishPageSlist](MiReplenishPageSlist_function_003BADE0.md) at `0x003BAECD`
- [MiFreeListPageContentsChanged](MiFreeListPageContentsChanged_function_003BD4BC.md) at `0x003BD527`
- [MiWalkAllFreeZeroLists](../4B/MiWalkAllFreeZeroLists_function_004BB6C8.md) at `0x004BB795`

### Static image references
- `0x003BB8D3` → RVA `0x00FC5002` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003BB8B0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003BB8B5  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
003BB8BA  44 8B D2                        mov r10d, edx
003BB8BD  4D 63 D9                        movsxd r11, r9d
003BB8C0  41 C1 EA 10                     shr r10d, 0x10
003BB8C4  8B C2                           mov eax, edx
003BB8C6  C1 E8 0F                        shr eax, 0xf
003BB8C9  41 83 E2 03                     and r10d, 3
003BB8CD  83 E0 01                        and eax, 1
003BB8D0  49 63 D8                        movsxd rbx, r8d
003BB8D3  80 3D 28 97 C0 00 01            cmp byte ptr [rip + 0xc09728], 1
003BB8DA  48 8B F9                        mov rdi, rcx
003BB8DD  77 2B                           ja 0x1403bb90a
003BB8DF  45 33 C9                        xor r9d, r9d
003BB8E2  4B 8D 14 92                     lea rdx, [r10 + r10*4]
003BB8E6  4C 8D 04 50                     lea r8, [rax + rdx*2]
003BB8EA  4A 8D 0C 43                     lea rcx, [rbx + r8*2]
003BB8EE  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
003BB8F3  49 8D 14 49                     lea rdx, [r9 + rcx*2]
003BB8F7  49 8D 04 93                     lea rax, [r11 + rdx*4]
003BB8FB  48 8B 84 C7 E0 03 00 00         mov rax, qword ptr [rdi + rax*8 + 0x3e0]
003BB903  48 8B 7C 24 10                  mov rdi, qword ptr [rsp + 0x10]
003BB908  C3                              ret
003BB909  CC                              int3
003BB90A  44 8B CA                        mov r9d, edx
003BB90D  49 C1 E9 08                     shr r9, 8
003BB911  41 83 E1 01                     and r9d, 1
003BB915  EB CB                           jmp 0x1403bb8e2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetColorHeadBase(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_r10 = (unsigned int)(((unsigned int)(a2)) >> (16));
    result = (unsigned int)(((unsigned int)(a2)) >> (15));
    v_r10 = (unsigned int)((v_r10) & (3));
    result = (unsigned int)((result) & (1));
    if ((*(unsigned __int8 *)(v_rip + 12621608)) > 1) goto loc_003BB90A;
    a4 = 0;
loc_003BB8E2:
    return *(unsigned __int64 *)(a1 + (int)(a4) + a4 + (int)(a3) + result + v_r10 + v_r10 * 4 * 2 * 2 * 2 * 4 * 8 + 992);
loc_003BB90A:
    a4 = ((unsigned int)((unsigned int)(a4 + (int)(a3) + result + v_r10 + v_r10 * 4 * 2 * 2 * 2))) >> (8);
    a4 = (unsigned int)((a4) & (1));
    goto loc_003BB8E2;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetColorHeadBase(void *Arg1, int32_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_r10 = (uint32_t)(((uint32_t)(Arg2)) >> (16));
    result = (uint32_t)(((uint32_t)(Arg2)) >> (15));
    local_r10 = (uint32_t)((local_r10) & (3));
    result = (uint32_t)((result) & (1));
    if ((*(uint8_t *)(v_rip + 0xC09728)) > 1) goto loc_003BB90A;
    Arg4 = 0;
loc_003BB8E2:
    return *(uint64_t *)(arg1 + (int32_t)(arg4) + arg4 + (int32_t)(arg3) + result + local_r10 + local_r10 * 4 * 2 * 2 * 2 * 4 * 8 + 0x3E0);
loc_003BB90A:
    Arg4 = ((uint32_t)((uint32_t)(Arg4 + (int32_t)(Arg3) + result + local_r10 + local_r10 * 4 * 2 * 2 * 2))) >> (8);
    Arg4 = (uint32_t)((Arg4) & (1));
    goto loc_003BB8E2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x3E0 + rax*8` | `64` | `R` |
| `Arg3` | `+ 0x0 + r8*2` | `64` | `R` |
| `Arg4` | `+ 0x0 + rdx*4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003BB8B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003BB8B0[BB_003BB8B0]
  bb_003BB8DF[BB_003BB8DF]
  bb_003BB8E2[BB_003BB8E2]
  bb_003BB909[BB_003BB909]
  bb_003BB90A[BB_003BB90A]
  bb_003BB8B0 -->|branch| bb_003BB90A
  bb_003BB8B0 -->|fallthrough| bb_003BB8DF
  bb_003BB8DF -->|flow| bb_003BB8E2
  bb_003BB909 -->|flow| bb_003BB90A
  bb_003BB90A -->|branch| bb_003BB8E2
```
