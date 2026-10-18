# ViAvlAcquireTableLockAtDpcLevel

- RVA: `0x003EF7D4`–`0x003EF837` (길이 `99` bytes)
- VA: `0x00000001403EF7D4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096B48`
- 디코드: `28`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003EF7FC` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x003EF829` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)

### Direct callers
- [ViAvlAcquireTableLockAtDpcLevelSafe](ViAvlAcquireTableLockAtDpcLevelSafe_function_003EF3A0.md) at `0x003EF3DB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EF7D4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003EF7D9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
003EF7DE  57                              push rdi
003EF7DF  48 83 EC 20                     sub rsp, 0x20
003EF7E3  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
003EF7EC  48 8B F9                        mov rdi, rcx
003EF7EF  48 83 E9 80                     sub rcx, -0x80
003EF7F3  48 8B DA                        mov rbx, rdx
003EF7F6  F6 42 0C 04                     test byte ptr [rdx + 0xc], 4
003EF7FA  75 2D                           jne 0x1403ef829
003EF7FC  E8 2F 96 E5 FF                  call 0x140248e30
003EF801  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
003EF804  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003EF809  48 89 3B                        mov qword ptr [rbx], rdi
003EF80C  8D 48 01                        lea ecx, [rax + 1]
003EF80F  33 C8                           xor ecx, eax
003EF811  83 E1 0F                        and ecx, 0xf
003EF814  33 C8                           xor ecx, eax
003EF816  80 4B 0C 02                     or byte ptr [rbx + 0xc], 2
003EF81A  89 4B 10                        mov dword ptr [rbx + 0x10], ecx
003EF81D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003EF822  48 83 C4 20                     add rsp, 0x20
003EF826  5F                              pop rdi
003EF827  C3                              ret
003EF828  CC                              int3
003EF829  E8 52 96 E5 FF                  call 0x140248e80
003EF82E  48 89 B7 88 00 00 00            mov qword ptr [rdi + 0x88], rsi
003EF835  EB CA                           jmp 0x1403ef801
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViAvlAcquireTableLockAtDpcLevel(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a1 = (a1) - (-128);
    if (((*(unsigned __int8 *)(a2 + 12)) & (4)) != 0) goto loc_003EF829;
    result = ExAcquireSpinLockSharedAtDpcLevel(a1, a2, a3, a4);
loc_003EF801:
    *(unsigned __int64 *)(a2) = a1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16)) + 1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))));
    a1 = (unsigned int)((a1) & (15));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))));
    *(unsigned int *)(a2 + 16) = (unsigned int)(a1);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(*(unsigned int *)(a2 + 16));
loc_003EF829:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a1, a2, a3, a4);
    *(unsigned __int64 *)(a1 + 136) = v_stack_p10;
    goto loc_003EF801;
}
```

## 5. (Beta) C Style

```c
int64_t ViAvlAcquireTableLockAtDpcLevel(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) - (-128);
    if (((*(uint8_t *)(arg2 + 0xC)) & (4)) != 0) goto loc_003EF829;
    result = ExAcquireSpinLockSharedAtDpcLevel(Arg1, Arg2, a3, a4);
loc_003EF801:
    *(void **)(arg2) = Arg1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + 1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))));
    Arg1 = (uint32_t)((Arg1) & (15));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))));
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)(Arg1);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(*(uint32_t *)(arg2 + 0x10));
loc_003EF829:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1, Arg2, a3, a4);
    *(uint64_t *)(arg1 + 0x88) = v_stack_p10;
    goto loc_003EF801;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x88` | `64` | `W` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0xC` | `8` | `R` |
| `Arg2` | `+ 0xC` | `8` | `R/W` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x10` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EF7D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EF7D4[BB_003EF7D4]
  bb_003EF7FC[BB_003EF7FC]
  bb_003EF801[BB_003EF801]
  bb_003EF828[BB_003EF828]
  bb_003EF829[BB_003EF829]
  bb_003EF7D4 -->|branch| bb_003EF829
  bb_003EF7D4 -->|fallthrough| bb_003EF7FC
  bb_003EF7FC -->|flow| bb_003EF801
  bb_003EF828 -->|flow| bb_003EF829
  bb_003EF829 -->|branch| bb_003EF801
```
