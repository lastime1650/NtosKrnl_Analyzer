# IoInitializeIrpPriv

- RVA: `0x00443710`–`0x004437A4` (길이 `148` bytes)
- VA: `0x0000000140443710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065C48`
- 디코드: `38`개 명령, `148/148` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0044373B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0044379D` → [IovInitializeIrp](../../pagevrfy/BB/IovInitializeIrp_function_00BB9418.md) (function, `0x00BB9418`)

### Direct callers
- [IoInitializeIrpEx](IoInitializeIrpEx_function_004436B0.md) at `0x004436CA`

### Static image references
- `0x0044371F` → RVA `0x00F04A20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0044379D` → [IovInitializeIrp](../../pagevrfy/BB/IovInitializeIrp_function_00BB9418.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00443710  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00443715  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0044371A  57                              push rdi
0044371B  48 83 EC 20                     sub rsp, 0x20
0044371F  8B 05 FB 12 AC 00               mov eax, dword ptr [rip + 0xac12fb]
00443725  48 8B D9                        mov rbx, rcx
00443728  49 0F BE F8                     movsx rdi, r8b
0044372C  0F B7 F2                        movzx esi, dx
0044372F  A8 10                           test al, 0x10
00443731  75 65                           jne 0x140443798
00443733  4C 8B C6                        mov r8, rsi
00443736  33 D2                           xor edx, edx
00443738  48 8B CB                        mov rcx, rbx
0044373B  E8 00 35 28 00                  call 0x1406c6c40
00443740  66 89 73 02                     mov word ptr [rbx + 2], si
00443744  8D 47 01                        lea eax, [rdi + 1]
00443747  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0044374C  88 43 43                        mov byte ptr [rbx + 0x43], al
0044374F  66 C7 03 06 00                  mov word ptr [rbx], 6
00443754  40 88 7B 42                     mov byte ptr [rbx + 0x42], dil
00443758  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00443761  0F B6 88 4A 02 00 00            movzx ecx, byte ptr [rax + 0x24a]
00443768  48 8D 43 20                     lea rax, [rbx + 0x20]
0044376C  88 4B 46                        mov byte ptr [rbx + 0x46], cl
0044376F  48 89 40 08                     mov qword ptr [rax + 8], rax
00443773  48 89 00                        mov qword ptr [rax], rax
00443776  48 8D 04 FD 1A 00 00 00         lea rax, [rdi*8 + 0x1a]
0044377E  48 03 C7                        add rax, rdi
00443781  48 8D 04 C3                     lea rax, [rbx + rax*8]
00443785  48 89 83 B8 00 00 00            mov qword ptr [rbx + 0xb8], rax
0044378C  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00443791  48 83 C4 20                     add rsp, 0x20
00443795  5F                              pop rdi
00443796  C3                              ret
00443797  CC                              int3
00443798  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0044379D  E8 76 5C 77 00                  call 0x140bb9418
004437A2  EB 8F                           jmp 0x140443733
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoInitializeIrpPriv(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11277051)))) & (16)) != 0) goto loc_00443798;
loc_00443733:
    a2 = 0;
    result = memset(a1, a2, (unsigned __int16)(a2), a4);
    *(unsigned __int16 *)(a1 + 2) = (unsigned __int16)((unsigned __int16)(a2));
    *(unsigned __int8 *)(a1 + 67) = (unsigned __int8)((__int8)(a3) + 1);
    *(unsigned __int16 *)(a1) = 6;
    *(unsigned __int8 *)(a1 + 66) = (unsigned __int8)((__int8)(a3));
    *(unsigned __int8 *)(a1 + 70) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586));
    *(unsigned __int64 *)(a1 + 32 + 8) = a1 + 32;
    *(unsigned __int64 *)(a1 + 32) = a1 + 32;
    result = ((__int8)(a3) * 8 + 26) + ((__int8)(a3));
    *(unsigned __int64 *)(a1 + 184) = a1 + result * 8;
    v_rsp = (v_rsp) + (32);
    return a1 + result * 8;
loc_00443798:
    result = IovInitializeIrp(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586), a2, (unsigned __int16)(a2), v_stack_p28);
    goto loc_00443733;
}
```

## 5. (Beta) C Style

```c
int64_t IoInitializeIrpPriv(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAC12FB)))) & (16)) != 0) goto loc_00443798;
loc_00443733:
    Arg2 = 0;
    result = memset(Arg1, Arg2, (uint16_t)(Arg2), a4);
    *(uint16_t *)(arg1 + 0x2) = (uint16_t)((uint16_t)(Arg2));
    *(uint8_t *)(arg1 + 0x43) = (uint8_t)((int8_t)(Arg3) + 1);
    *(uint16_t *)(arg1) = 6;
    *(uint8_t *)(arg1 + 0x42) = (uint8_t)((int8_t)(Arg3));
    *(uint8_t *)(arg1 + 0x46) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A));
    *(void **)(arg1 + 0x20 + 0x8) = Arg1 + 32;
    *(void **)(arg1 + 0x20) = Arg1 + 32;
    result = ((int8_t)(Arg3) * 8 + 26) + ((int8_t)(Arg3));
    *(void **)(arg1 + 0xB8) = Arg1 + result * 8;
    local_rsp = (local_rsp) + (32);
    return Arg1 + result * 8;
loc_00443798:
    result = IovInitializeIrp(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A), Arg2, (uint16_t)(Arg2), v_stack_p28);
    goto loc_00443733;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x2` | `16` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x42` | `8` | `W` |
| `Arg1` | `+ 0x43` | `8` | `W` |
| `Arg1` | `+ 0x46` | `8` | `W` |
| `Arg1` | `+ 0xB8` | `64` | `W` |
| `Arg3` | `+ 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00443710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00443710[BB_00443710]
  bb_00443733[BB_00443733]
  bb_00443797[BB_00443797]
  bb_00443798[BB_00443798]
  bb_00443710 -->|branch| bb_00443798
  bb_00443710 -->|fallthrough| bb_00443733
  bb_00443797 -->|flow| bb_00443798
  bb_00443798 -->|branch| bb_00443733
```
