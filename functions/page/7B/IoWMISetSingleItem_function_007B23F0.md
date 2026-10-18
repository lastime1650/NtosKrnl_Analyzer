# IoWMISetSingleItem

- RVA: `0x007B23F0`–`0x007B250F` (길이 `287` bytes)
- VA: `0x00000001407B23F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE68C`
- 디코드: `86`개 명령, `287/287` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007B2450` → [WmipAllocateSingleInstanceWnode](../A9/WmipAllocateSingleInstanceWnode_function_00A9E2B0.md) (function, `0x00A9E2B0`)
- `0x007B249C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007B24B6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007B24DD` → [WmipQuerySetExecuteSI](../9E/WmipQuerySetExecuteSI_function_009E0574.md) (function, `0x009E0574`)
- `0x007B24E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007B249C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007B24B6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007B24E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B23F0  4C 8B DC                        mov r11, rsp
007B23F3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
007B23F7  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
007B23FB  49 89 7B 18                     mov qword ptr [r11 + 0x18], rdi
007B23FF  55                              push rbp
007B2400  41 54                           push r12
007B2402  41 55                           push r13
007B2404  41 56                           push r14
007B2406  41 57                           push r15
007B2408  48 8B EC                        mov rbp, rsp
007B240B  48 83 EC 60                     sub rsp, 0x60
007B240F  44 8B 75 50                     mov r14d, dword ptr [rbp + 0x50]
007B2413  48 8D 45 F0                     lea rax, [rbp - 0x10]
007B2417  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
007B241B  33 FF                           xor edi, edi
007B241D  48 8D 45 E0                     lea rax, [rbp - 0x20]
007B2421  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
007B2425  49 89 43 A0                     mov qword ptr [r11 - 0x60], rax
007B2429  45 8B F9                        mov r15d, r9d
007B242C  48 8D 45 E8                     lea rax, [rbp - 0x18]
007B2430  89 7D E0                        mov dword ptr [rbp - 0x20], edi
007B2433  45 8B E0                        mov r12d, r8d
007B2436  49 89 43 98                     mov qword ptr [r11 - 0x68], rax
007B243A  4C 8B E9                        mov r13, rcx
007B243D  89 7D E4                        mov dword ptr [rbp - 0x1c], edi
007B2440  4C 8D 4D E4                     lea r9, [rbp - 0x1c]
007B2444  89 7D E8                        mov dword ptr [rbp - 0x18], edi
007B2447  45 8B C6                        mov r8d, r14d
007B244A  8D 4F 44                        lea ecx, [rdi + 0x44]
007B244D  48 8B F2                        mov rsi, rdx
007B2450  E8 5B BE 2E 00                  call 0x140a9e2b0
007B2455  8B D8                           mov ebx, eax
007B2457  85 C0                           test eax, eax
007B2459  0F 88 8F 00 00 00               js 0x1407b24ee
007B245F  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
007B2463  8B 45 E4                        mov eax, dword ptr [rbp - 0x1c]
007B2466  8B 5D E0                        mov ebx, dword ptr [rbp - 0x20]
007B2469  C7 47 2C 04 00 00 00            mov dword ptr [rdi + 0x2c], 4
007B2470  48 83 67 10 00                  and qword ptr [rdi + 0x10], 0
007B2475  48 8D 0C 07                     lea rcx, [rdi + rax]
007B2479  89 1F                           mov dword ptr [rdi], ebx
007B247B  83 67 0C 00                     and dword ptr [rdi + 0xc], 0
007B247F  44 89 7F 08                     mov dword ptr [rdi + 8], r15d
007B2483  44 89 67 38                     mov dword ptr [rdi + 0x38], r12d
007B2487  89 47 30                        mov dword ptr [rdi + 0x30], eax
007B248A  0F B7 06                        movzx eax, word ptr [rsi]
007B248D  66 89 01                        mov word ptr [rcx], ax
007B2490  48 83 C1 02                     add rcx, 2
007B2494  44 0F B7 06                     movzx r8d, word ptr [rsi]
007B2498  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
007B249C  E8 9F 43 F1 FF                  call 0x1406c6840
007B24A1  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
007B24A4  45 8B C6                        mov r8d, r14d
007B24A7  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
007B24AB  44 89 77 40                     mov dword ptr [rdi + 0x40], r14d
007B24AF  89 47 3C                        mov dword ptr [rdi + 0x3c], eax
007B24B2  48 8D 0C 07                     lea rcx, [rdi + rax]
007B24B6  E8 85 43 F1 FF                  call 0x1406c6840
007B24BB  8B 07                           mov eax, dword ptr [rdi]
007B24BD  41 B1 03                        mov r9b, 3
007B24C0  89 45 E8                        mov dword ptr [rbp - 0x18], eax
007B24C3  45 33 C0                        xor r8d, r8d
007B24C6  48 8D 45 E8                     lea rax, [rbp - 0x18]
007B24CA  33 D2                           xor edx, edx
007B24CC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007B24D1  49 8B CD                        mov rcx, r13
007B24D4  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
007B24D8  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007B24DD  E8 92 E0 22 00                  call 0x1409e0574
007B24E2  33 D2                           xor edx, edx
007B24E4  48 8B CF                        mov rcx, rdi
007B24E7  8B D8                           mov ebx, eax
007B24E9  E8 82 03 3D 00                  call 0x140b82870
007B24EE  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
007B24F3  8B C3                           mov eax, ebx
007B24F5  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
007B24F9  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
007B24FD  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
007B2501  49 8B E3                        mov rsp, r11
007B2504  41 5F                           pop r15
007B2506  41 5E                           pop r14
007B2508  41 5D                           pop r13
007B250A  41 5C                           pop r12
007B250C  5D                              pop rbp
007B250D  C3                              ret
007B250E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoWMISetSingleItem(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (96);
    *(unsigned __int64 *)(v_rsp - 88) = v_stack_m38;
    v_rdi = 0;
    v_stack_m38 = 0;
    *(unsigned __int64 *)(v_rsp - 96) = v_stack_m48;
    v_stack_m48 = 0;
    *(unsigned __int64 *)(v_rsp - 104) = v_stack_m40;
    v_stack_m44 = 0;
    v_stack_m40 = 0;
    result = WmipAllocateSingleInstanceWnode(v_rdi + 68, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m44);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        v_rdi = v_stack_m38;
        result = v_stack_m44;
        v_rbx = v_stack_m48;
        *(unsigned int *)(v_rdi + 44) = 4;
        a1 = v_rdi + result * 1;
        *(unsigned int *)(v_rdi) = (unsigned int)(v_rbx);
        *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(a4));
        *(unsigned int *)(v_rdi + 56) = (unsigned int)((unsigned int)(a3));
        *(unsigned int *)(v_rdi + 48) = (unsigned int)(result);
        result = *(unsigned __int16 *)(a2);
        *(unsigned __int16 *)(a1) = (unsigned __int16)(result);
        a1 = (a1) + (2);
        a3 = *(unsigned __int16 *)(a2);
        a2 = *(unsigned __int64 *)(a2 + 8);
        result = memcpy(a1, a2, a3, v_stack_m44);
        result = v_stack_m40;
        a3 = (unsigned int)((unsigned int)(a5));
        a2 = a6;
        *(unsigned int *)(v_rdi + 64) = (unsigned int)((unsigned int)(a5));
        *(unsigned int *)(v_rdi + 60) = (unsigned int)(result);
        a1 = v_rdi + result * 1;
        result = memcpy(a1, a2, a3, v_stack_m44);
        result = *(unsigned int *)(v_rdi);
        a4 = 3;
        v_stack_m40 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_m40;
        a2 = 0;
        v_stack_m58 = result;
        a1 = a1;
        v_stack_m60 = (unsigned int)(v_rbx);
        v_stack_m68 = v_rdi;
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
int64_t IoWMISetSingleItem(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (96);
    *(uint64_t *)(local_rsp - 0x58) = v_stack_m38;
    local_rdi = 0;
    v_stack_m38 = 0;
    *(uint64_t *)(local_rsp - 0x60) = v_stack_m48;
    v_stack_m48 = 0;
    *(uint64_t *)(local_rsp - 0x68) = v_stack_m40;
    v_stack_m44 = 0;
    v_stack_m40 = 0;
    result = WmipAllocateSingleInstanceWnode(local_rdi + 68, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m44);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        local_rdi = v_stack_m38;
        result = v_stack_m44;
        local_rbx = v_stack_m48;
        *(uint32_t *)(local_rdi + 0x2C) = 4;
        Arg1 = local_rdi + result * 1;
        *(uint32_t *)(local_rdi) = (uint32_t)(local_rbx);
        *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(Arg4));
        *(uint32_t *)(local_rdi + 0x38) = (uint32_t)((uint32_t)(Arg3));
        *(uint32_t *)(local_rdi + 0x30) = (uint32_t)(result);
        result = *(uint16_t *)(arg2);
        *(uint16_t *)(Arg1) = (uint16_t)(result);
        Arg1 = (Arg1) + (2);
        Arg3 = *(uint16_t *)(arg2);
        Arg2 = *(uint64_t *)(arg2 + 0x8);
        result = memcpy(Arg1, Arg2, Arg3, v_stack_m44);
        result = v_stack_m40;
        Arg3 = (uint32_t)((uint32_t)(Arg5));
        Arg2 = Arg6;
        *(uint32_t *)(local_rdi + 0x40) = (uint32_t)((uint32_t)(Arg5));
        *(uint32_t *)(local_rdi + 0x3C) = (uint32_t)(result);
        Arg1 = local_rdi + result * 1;
        result = memcpy(Arg1, Arg2, Arg3, v_stack_m44);
        result = *(uint32_t *)(local_rdi);
        Arg4 = 3;
        v_stack_m40 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_m40;
        Arg2 = 0;
        v_stack_m58 = result;
        Arg1 = Arg1;
        v_stack_m60 = (uint32_t)(local_rbx);
        v_stack_m68 = local_rdi;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B23F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B23F0[BB_007B23F0]
  bb_007B245F[BB_007B245F]
  bb_007B24EE[BB_007B24EE]
  bb_007B250E[BB_007B250E]
  bb_007B23F0 -->|branch| bb_007B24EE
  bb_007B23F0 -->|fallthrough| bb_007B245F
  bb_007B245F -->|flow| bb_007B24EE
```
