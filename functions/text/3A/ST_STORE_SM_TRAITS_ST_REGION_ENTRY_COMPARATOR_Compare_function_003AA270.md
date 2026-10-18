# ST_STORE&lt;SM_TRAITS&gt;::ST_REGION_ENTRY_COMPARATOR::Compare

- RVA: `0x003AA270`–`0x003AA33A` (길이 `202` bytes)
- VA: `0x00000001403AA270`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008B784`
- 디코드: `59`개 명령, `202/202` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [B_TREE&lt;unsigned long,ST_STORE&lt;SM_TRAITS&gt;::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE&lt;SM_TRAITS&gt;::ST_REGION_ENTRY_COMPARATOR&gt;::BTreeChangeKey](B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003A9D80.md) at `0x003AA055`
- [B_TREE&lt;unsigned long,ST_STORE&lt;SM_TRAITS&gt;::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE&lt;SM_TRAITS&gt;::ST_REGION_ENTRY_COMPARATOR&gt;::BTreeChangeKey](B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003A9D80.md) at `0x003AA092`
- [B_TREE&lt;unsigned long,ST_STORE&lt;SM_TRAITS&gt;::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE&lt;SM_TRAITS&gt;::ST_REGION_ENTRY_COMPARATOR&gt;::BTreeChangeKey](B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003A9D80.md) at `0x003AA111`
- [B_TREE&lt;unsigned long,ST_STORE&lt;SM_TRAITS&gt;::_ST_REGION_ENTRY,4096,NP_CONTEXT,ST_STORE&lt;SM_TRAITS&gt;::ST_REGION_ENTRY_COMPARATOR&gt;::BTreeChangeKey](B_TREE_unsigned_long_ST_STORE_SM_TRAITS__ST_REGION_ENTRY_4096_NP_CONTEXT_ST_STORE_SM_TRAITS_ST_REGIO_function_003A9D80.md) at `0x003AA1A8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003AA270  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003AA275  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
003AA27A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
003AA27F  57                              push rdi
003AA280  41 54                           push r12
003AA282  41 55                           push r13
003AA284  41 56                           push r14
003AA286  41 57                           push r15
003AA288  41 8B 28                        mov ebp, dword ptr [r8]
003AA28B  4C 8B E9                        mov r13, rcx
003AA28E  8B 89 88 01 00 00               mov ecx, dword ptr [rcx + 0x188]
003AA294  8B DD                           mov ebx, ebp
003AA296  8B 32                           mov esi, dword ptr [rdx]
003AA298  41 B9 01 00 00 00               mov r9d, 1
003AA29E  D3 EB                           shr ebx, cl
003AA2A0  45 8B C1                        mov r8d, r9d
003AA2A3  45 8B A5 8C 01 00 00            mov r12d, dword ptr [r13 + 0x18c]
003AA2AA  44 8B DE                        mov r11d, esi
003AA2AD  45 8B B5 90 01 00 00            mov r14d, dword ptr [r13 + 0x190]
003AA2B4  33 C0                           xor eax, eax
003AA2B6  45 8B BD 98 01 00 00            mov r15d, dword ptr [r13 + 0x198]
003AA2BD  41 D3 EB                        shr r11d, cl
003AA2C0  45 0F BD D3                     bsr r10d, r11d
003AA2C4  0F BD FB                        bsr edi, ebx
003AA2C7  4B 8B 94 D5 80 00 00 00         mov rdx, qword ptr [r13 + r10*8 + 0x80]
003AA2CF  41 8B CA                        mov ecx, r10d
003AA2D2  41 D3 E0                        shl r8d, cl
003AA2D5  41 8B CC                        mov ecx, r12d
003AA2D8  23 CE                           and ecx, esi
003AA2DA  4D 33 C3                        xor r8, r11
003AA2DD  41 0F AF CE                     imul ecx, r14d
003AA2E1  4D 03 C0                        add r8, r8
003AA2E4  44 23 E5                        and r12d, ebp
003AA2E7  45 0F AF E6                     imul r12d, r14d
003AA2EB  4A 03 0C C2                     add rcx, qword ptr [rdx + r8*8]
003AA2EF  49 8B 94 FD 80 00 00 00         mov rdx, qword ptr [r13 + rdi*8 + 0x80]
003AA2F7  46 8B 14 39                     mov r10d, dword ptr [rcx + r15]
003AA2FB  8B CF                           mov ecx, edi
003AA2FD  41 D3 E1                        shl r9d, cl
003AA300  45 8B C1                        mov r8d, r9d
003AA303  4C 33 C3                        xor r8, rbx
003AA306  41 8B CC                        mov ecx, r12d
003AA309  4D 03 C0                        add r8, r8
003AA30C  4A 03 0C C2                     add rcx, qword ptr [rdx + r8*8]
003AA310  46 3B 14 39                     cmp r10d, dword ptr [rcx + r15]
003AA314  73 1F                           jae 0x1403aa335
003AA316  B8 FF FF FF FF                  mov eax, 0xffffffff
003AA31B  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
003AA320  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
003AA325  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
003AA32A  41 5F                           pop r15
003AA32C  41 5E                           pop r14
003AA32E  41 5D                           pop r13
003AA330  41 5C                           pop r12
003AA332  5F                              pop rdi
003AA333  C3                              ret
003AA334  CC                              int3
003AA335  0F 97 C0                        seta al
003AA338  EB E1                           jmp 0x1403aa31b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___ST_REGION_ENTRY_COMPARATOR__Compare(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbx;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 392)))));
    result = 0;
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 392)))));
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r10)))));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 396))))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2)))));
    a3 = (a3) ^ (v_r11);
    a1 = (unsigned int)((a1) * ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 400)))));
    a3 = (a3) + (a3);
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 396))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a3)))));
    v_r12 = (unsigned int)((v_r12) * ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 400)))));
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_r10 * 8 + 128) + a3 * 8));
    a4 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    a3 = ((unsigned int)((unsigned int)(a4))) ^ (v_rbx);
    a3 = (a3) + (a3);
    a1 = ((unsigned int)((unsigned int)(v_r12))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_rdi * 8 + 128) + a3 * 8));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(a1 + 408)) * 1)))) >= (*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(a1 + 408)) * 1))) goto loc_003AA335;
loc_003AA31B:
    return (unsigned int)(0xFFFFFFFFULL);
loc_003AA335:
    result = (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(a1 + 408)) * 1)))) > (*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(a1 + 408)) * 1))) ? 1 : 0;
    goto loc_003AA31B;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___ST_REGION_ENTRY_COMPARATOR__Compare(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbx;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3))))) >> ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x188)))));
    result = 0;
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) >> ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x188)))));
    Arg3 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_r10)))));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18C))))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))));
    Arg3 = (Arg3) ^ (local_r11);
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x190)))));
    Arg3 = (Arg3) + (Arg3);
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18C))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg3)))));
    local_r12 = (uint32_t)((local_r12) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x190)))));
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(arg1 + local_r10 * 8 + 0x80) + arg3 * 8));
    a4 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    Arg3 = ((uint32_t)((uint32_t)(a4))) ^ (local_rbx);
    Arg3 = (Arg3) + (Arg3);
    Arg1 = ((uint32_t)((uint32_t)(local_r12))) + (*(uint64_t *)(*(uint64_t *)(arg1 + local_rdi * 8 + 0x80) + arg3 * 8));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x198)) * 1)))) >= (*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x198)) * 1))) goto loc_003AA335;
loc_003AA31B:
    return (uint32_t)(0xFFFFFFFFULL);
loc_003AA335:
    result = (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x198)) * 1)))) > (*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x198)) * 1))) ? 1 : 0;
    goto loc_003AA31B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x80 + r10*8` | `64` | `R` |
| `Arg1` | `+ 0x80 + rdi*8` | `64` | `R` |
| `Arg1` | `+ 0x188` | `32` | `R` |
| `Arg1` | `+ 0x18C` | `32` | `R` |
| `Arg1` | `+ 0x190` | `32` | `R` |
| `Arg1` | `+ 0x198` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003AA270&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003AA270[BB_003AA270]
  bb_003AA316[BB_003AA316]
  bb_003AA31B[BB_003AA31B]
  bb_003AA334[BB_003AA334]
  bb_003AA335[BB_003AA335]
  bb_003AA270 -->|branch| bb_003AA335
  bb_003AA270 -->|fallthrough| bb_003AA316
  bb_003AA316 -->|flow| bb_003AA31B
  bb_003AA334 -->|flow| bb_003AA335
  bb_003AA335 -->|branch| bb_003AA31B
```
