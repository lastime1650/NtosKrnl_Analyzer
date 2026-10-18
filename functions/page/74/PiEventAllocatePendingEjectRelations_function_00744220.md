# PiEventAllocatePendingEjectRelations

- RVA: `0x00744220`–`0x007442AE` (길이 `142` bytes)
- VA: `0x0000000140744220`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060300`
- 디코드: `40`개 명령, `142/142` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00744259` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0074426D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)

### Direct callers
- [sub_00B33FE8](../B3/Unknown_function_00B33FE8.md) at `0x00B343CD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00744259` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0074426D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00744220  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00744225  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0074422A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0074422F  57                              push rdi
00744230  41 56                           push r14
00744232  41 57                           push r15
00744234  48 83 EC 20                     sub rsp, 0x20
00744238  48 8B B1 A0 00 00 00            mov rsi, qword ptr [rcx + 0xa0]
0074423F  4C 8B FA                        mov r15, rdx
00744242  BA 70 00 00 00                  mov edx, 0x70
00744247  45 8A F0                        mov r14b, r8b
0074424A  48 8B F9                        mov rdi, rcx
0074424D  41 B8 50 70 20 20               mov r8d, 0x20207050
00744253  49 8B E9                        mov rbp, r9
00744256  8D 4A D0                        lea ecx, [rdx - 0x30]
00744259  E8 92 DE 43 00                  call 0x140b820f0
0074425E  48 8B D8                        mov rbx, rax
00744261  48 85 C0                        test rax, rax
00744264  74 2B                           je 0x140744291
00744266  48 8B CE                        mov rcx, rsi
00744269  48 89 78 30                     mov qword ptr [rax + 0x30], rdi
0074426D  E8 AE B7 AC FF                  call 0x14020fa20
00744272  48 89 73 38                     mov qword ptr [rbx + 0x38], rsi
00744276  4C 89 7B 40                     mov qword ptr [rbx + 0x40], r15
0074427A  44 88 73 58                     mov byte ptr [rbx + 0x58], r14b
0074427E  8B 8F 98 00 00 00               mov ecx, dword ptr [rdi + 0x98]
00744284  C1 E9 03                        shr ecx, 3
00744287  80 E1 01                        and cl, 1
0074428A  48 89 6B 60                     mov qword ptr [rbx + 0x60], rbp
0074428E  88 4B 59                        mov byte ptr [rbx + 0x59], cl
00744291  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00744296  48 8B C3                        mov rax, rbx
00744299  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0074429E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
007442A3  48 83 C4 20                     add rsp, 0x20
007442A7  41 5F                           pop r15
007442A9  41 5E                           pop r14
007442AB  5F                              pop rdi
007442AC  C3                              ret
007442AD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiEventAllocatePendingEjectRelations(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(112 - 48, 112, (unsigned int)(0x20207050ULL), a4);
    if (result != 0) {
        a1 = *(unsigned __int64 *)(a1 + 160);
        *(unsigned __int64 *)(result + 48) = a1;
        result = ObfReferenceObject(a1, 112, (unsigned int)(0x20207050ULL), a4);
        *(unsigned __int64 *)(result + 56) = *(unsigned __int64 *)(a1 + 160);
        *(unsigned __int64 *)(result + 64) = a2;
        *(unsigned __int8 *)(result + 88) = a3;
        a1 = *(unsigned int *)(a1 + 152);
        a1 = (unsigned int)((a1) >> (3));
        a1 = (unsigned __int8)((a1) & (1));
        *(unsigned __int64 *)(result + 96) = a4;
        *(unsigned __int8 *)(result + 89) = (unsigned __int8)(a1);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiEventAllocatePendingEjectRelations(void *Arg1, int64_t Arg2, uint8_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(112 - 48, 112, (uint32_t)(0x20207050ULL), Arg4);
    if (result != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0xA0);
        *(void **)(result + 0x30) = Arg1;
        result = ObfReferenceObject(Arg1, 112, (uint32_t)(0x20207050ULL), Arg4);
        *(uint64_t *)(result + 0x38) = *(uint64_t *)(arg1 + 0xA0);
        *(uint64_t *)(result + 0x40) = Arg2;
        *(uint8_t *)(result + 0x58) = Arg3;
        Arg1 = *(uint32_t *)(arg1 + 0x98);
        Arg1 = (uint32_t)((Arg1) >> (3));
        Arg1 = (uint8_t)((Arg1) & (1));
        *(uint64_t *)(result + 0x60) = Arg4;
        *(uint8_t *)(result + 0x59) = (uint8_t)(Arg1);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x98` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00744220&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00744220[BB_00744220]
  bb_00744266[BB_00744266]
  bb_00744291[BB_00744291]
  bb_007442AD[BB_007442AD]
  bb_00744220 -->|branch| bb_00744291
  bb_00744220 -->|fallthrough| bb_00744266
  bb_00744266 -->|flow| bb_00744291
```
