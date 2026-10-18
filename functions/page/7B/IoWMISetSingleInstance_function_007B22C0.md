# IoWMISetSingleInstance

- RVA: `0x007B22C0`–`0x007B23DB` (길이 `283` bytes)
- VA: `0x00000001407B22C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00092598`
- 디코드: `81`개 명령, `283/283` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007B2320` → [WmipAllocateSingleInstanceWnode](../A9/WmipAllocateSingleInstanceWnode_function_00A9E2B0.md) (function, `0x00A9E2B0`)
- `0x007B2368` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007B2382` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007B23A9` → [WmipQuerySetExecuteSI](../9E/WmipQuerySetExecuteSI_function_009E0574.md) (function, `0x009E0574`)
- `0x007B23B5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007B2368` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007B2382` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007B23B5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B22C0  4C 8B DC                        mov r11, rsp
007B22C3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
007B22C7  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
007B22CB  49 89 7B 18                     mov qword ptr [r11 + 0x18], rdi
007B22CF  4D 89 63 20                     mov qword ptr [r11 + 0x20], r12
007B22D3  55                              push rbp
007B22D4  41 56                           push r14
007B22D6  41 57                           push r15
007B22D8  48 8B EC                        mov rbp, rsp
007B22DB  48 83 EC 60                     sub rsp, 0x60
007B22DF  48 83 65 F0 00                  and qword ptr [rbp - 0x10], 0
007B22E4  48 8D 45 F0                     lea rax, [rbp - 0x10]
007B22E8  83 65 E0 00                     and dword ptr [rbp - 0x20], 0
007B22EC  45 8B F8                        mov r15d, r8d
007B22EF  83 65 E4 00                     and dword ptr [rbp - 0x1c], 0
007B22F3  4C 8B E1                        mov r12, rcx
007B22F6  83 65 E8 00                     and dword ptr [rbp - 0x18], 0
007B22FA  B9 40 00 00 00                  mov ecx, 0x40
007B22FF  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
007B2303  48 8B F2                        mov rsi, rdx
007B2306  45 8B F1                        mov r14d, r9d
007B2309  48 8D 45 E0                     lea rax, [rbp - 0x20]
007B230D  49 89 43 B0                     mov qword ptr [r11 - 0x50], rax
007B2311  4C 8D 4D E4                     lea r9, [rbp - 0x1c]
007B2315  48 8D 45 E8                     lea rax, [rbp - 0x18]
007B2319  45 8B C6                        mov r8d, r14d
007B231C  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
007B2320  E8 8B BF 2E 00                  call 0x140a9e2b0
007B2325  8B D8                           mov ebx, eax
007B2327  85 C0                           test eax, eax
007B2329  0F 88 8B 00 00 00               js 0x1407b23ba
007B232F  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
007B2333  8B 45 E4                        mov eax, dword ptr [rbp - 0x1c]
007B2336  8B 5D E0                        mov ebx, dword ptr [rbp - 0x20]
007B2339  C7 47 2C 02 00 00 00            mov dword ptr [rdi + 0x2c], 2
007B2340  48 83 67 10 00                  and qword ptr [rdi + 0x10], 0
007B2345  48 8D 0C 07                     lea rcx, [rdi + rax]
007B2349  89 1F                           mov dword ptr [rdi], ebx
007B234B  83 67 0C 00                     and dword ptr [rdi + 0xc], 0
007B234F  44 89 7F 08                     mov dword ptr [rdi + 8], r15d
007B2353  89 47 30                        mov dword ptr [rdi + 0x30], eax
007B2356  0F B7 06                        movzx eax, word ptr [rsi]
007B2359  66 89 01                        mov word ptr [rcx], ax
007B235C  48 83 C1 02                     add rcx, 2
007B2360  44 0F B7 06                     movzx r8d, word ptr [rsi]
007B2364  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
007B2368  E8 D3 44 F1 FF                  call 0x1406c6840
007B236D  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
007B2370  45 8B C6                        mov r8d, r14d
007B2373  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
007B2377  44 89 77 3C                     mov dword ptr [rdi + 0x3c], r14d
007B237B  89 47 38                        mov dword ptr [rdi + 0x38], eax
007B237E  48 8D 0C 07                     lea rcx, [rdi + rax]
007B2382  E8 B9 44 F1 FF                  call 0x1406c6840
007B2387  8B 07                           mov eax, dword ptr [rdi]
007B2389  41 B1 02                        mov r9b, 2
007B238C  89 45 E8                        mov dword ptr [rbp - 0x18], eax
007B238F  45 33 C0                        xor r8d, r8d
007B2392  48 8D 45 E8                     lea rax, [rbp - 0x18]
007B2396  33 D2                           xor edx, edx
007B2398  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007B239D  49 8B CC                        mov rcx, r12
007B23A0  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
007B23A4  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007B23A9  E8 C6 E1 22 00                  call 0x1409e0574
007B23AE  33 D2                           xor edx, edx
007B23B0  48 8B CF                        mov rcx, rdi
007B23B3  8B D8                           mov ebx, eax
007B23B5  E8 B6 04 3D 00                  call 0x140b82870
007B23BA  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
007B23BF  8B C3                           mov eax, ebx
007B23C1  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
007B23C5  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
007B23C9  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
007B23CD  4D 8B 63 38                     mov r12, qword ptr [r11 + 0x38]
007B23D1  49 8B E3                        mov rsp, r11
007B23D4  41 5F                           pop r15
007B23D6  41 5E                           pop r14
007B23D8  5D                              pop rbp
007B23D9  C3                              ret
007B23DA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoWMISetSingleInstance(__int64 a1, __int64 a2, int a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r12;
    v_rsp = (v_rsp) - (96);
    *(unsigned __int64 *)(v_rsp - 72) = v_stack_m28;
    *(unsigned __int64 *)(v_rsp - 80) = v_stack_m38;
    *(unsigned __int64 *)(v_rsp - 88) = v_stack_m30;
    result = WmipAllocateSingleInstanceWnode(64, a2, (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_m34);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        v_rdi = v_stack_m28;
        result = v_stack_m34;
        v_rbx = v_stack_m38;
        *(unsigned int *)(v_rdi + 44) = 2;
        a1 = v_rdi + result * 1;
        *(unsigned int *)(v_rdi) = (unsigned int)(v_rbx);
        *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(a3));
        *(unsigned int *)(v_rdi + 48) = (unsigned int)(result);
        result = *(unsigned __int16 *)(a2);
        *(unsigned __int16 *)(a1) = (unsigned __int16)(result);
        a1 = (a1) + (2);
        a3 = *(unsigned __int16 *)(a2);
        a2 = *(unsigned __int64 *)(a2 + 8);
        result = memcpy(a1, a2, a3, v_stack_m34);
        result = v_stack_m30;
        a3 = (unsigned int)((unsigned int)(a4));
        a2 = a5;
        *(unsigned int *)(v_rdi + 60) = (unsigned int)((unsigned int)(a4));
        *(unsigned int *)(v_rdi + 56) = (unsigned int)(result);
        a1 = v_rdi + result * 1;
        result = memcpy(a1, a2, a3, v_stack_m34);
        result = *(unsigned int *)(v_rdi);
        a4 = 2;
        v_stack_m30 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_m30;
        a2 = 0;
        v_stack_m48 = result;
        a1 = a1;
        v_stack_m50 = (unsigned int)(v_rbx);
        v_stack_m58 = v_rdi;
        result = WmipQuerySetExecuteSI(a1, a2, a3, a4);
        a2 = 0;
        a1 = v_rdi;
        v_rbx = (unsigned int)(result);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t IoWMISetSingleInstance(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r12;
    local_rsp = (local_rsp) - (96);
    *(uint64_t *)(local_rsp - 0x48) = v_stack_m28;
    *(uint64_t *)(local_rsp - 0x50) = v_stack_m38;
    *(uint64_t *)(local_rsp - 0x58) = v_stack_m30;
    result = WmipAllocateSingleInstanceWnode(64, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_m34);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        local_rdi = v_stack_m28;
        result = v_stack_m34;
        local_rbx = v_stack_m38;
        *(uint32_t *)(local_rdi + 0x2C) = 2;
        Arg1 = local_rdi + result * 1;
        *(uint32_t *)(local_rdi) = (uint32_t)(local_rbx);
        *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(Arg3));
        *(uint32_t *)(local_rdi + 0x30) = (uint32_t)(result);
        result = *(uint16_t *)(arg2);
        *(uint16_t *)(Arg1) = (uint16_t)(result);
        Arg1 = (Arg1) + (2);
        Arg3 = *(uint16_t *)(arg2);
        Arg2 = *(uint64_t *)(arg2 + 0x8);
        result = memcpy(Arg1, Arg2, Arg3, v_stack_m34);
        result = v_stack_m30;
        Arg3 = (uint32_t)((uint32_t)(Arg4));
        Arg2 = Arg5;
        *(uint32_t *)(local_rdi + 0x3C) = (uint32_t)((uint32_t)(Arg4));
        *(uint32_t *)(local_rdi + 0x38) = (uint32_t)(result);
        Arg1 = local_rdi + result * 1;
        result = memcpy(Arg1, Arg2, Arg3, v_stack_m34);
        result = *(uint32_t *)(local_rdi);
        Arg4 = 2;
        v_stack_m30 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_m30;
        Arg2 = 0;
        v_stack_m48 = result;
        Arg1 = Arg1;
        v_stack_m50 = (uint32_t)(local_rbx);
        v_stack_m58 = local_rdi;
        result = WmipQuerySetExecuteSI(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 0;
        Arg1 = local_rdi;
        local_rbx = (uint32_t)(result);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    return (uint32_t)((uint32_t)(local_rbx));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B22C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B22C0[BB_007B22C0]
  bb_007B232F[BB_007B232F]
  bb_007B23BA[BB_007B23BA]
  bb_007B23DA[BB_007B23DA]
  bb_007B22C0 -->|branch| bb_007B23BA
  bb_007B22C0 -->|fallthrough| bb_007B232F
  bb_007B232F -->|flow| bb_007B23BA
```
