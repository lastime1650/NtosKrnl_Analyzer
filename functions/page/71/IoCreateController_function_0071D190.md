# IoCreateController

- RVA: `0x0071D190`–`0x0071D2AD` (길이 `285` bytes)
- VA: `0x000000014071D190`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C7620`
- 디코드: `76`개 명령, `285/285` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0071D20E` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x0071D23B` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x0071D24A` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x0071D25E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0071D28B` → [KeInitializeDeviceQueue](../../text/4B/KeInitializeDeviceQueue_function_004B7F50.md) (function, `0x004B7F50`)

### Direct callers
- [DifIoCreateControllerWrapper](../../text/62/DifIoCreateControllerWrapper_function_00628AF0.md) at `0x00628BBA`

### Static image references
- `0x0071D1A6` → RVA `0x00E0A9C0` (`.data`; read)
- `0x0071D1E9` → RVA `0x00FC7320` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0071D25E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0071D28B` → [KeInitializeDeviceQueue](../../text/4B/KeInitializeDeviceQueue_function_004B7F50.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0071D190  4C 8B DC                        mov r11, rsp
0071D193  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0071D197  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0071D19B  55                              push rbp
0071D19C  48 8B EC                        mov rbp, rsp
0071D19F  48 81 EC 80 00 00 00            sub rsp, 0x80
0071D1A6  8B 05 14 D8 6E 00               mov eax, dword ptr [rip + 0x6ed814]
0071D1AC  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0071D1B0  33 DB                           xor ebx, ebx
0071D1B2  8B F9                           mov edi, ecx
0071D1B4  49 89 5B C0                     mov qword ptr [r11 - 0x40], rbx
0071D1B8  48 8D 4D 18                     lea rcx, [rbp + 0x18]
0071D1BC  49 89 4B B8                     mov qword ptr [r11 - 0x48], rcx
0071D1C0  F7 D8                           neg eax
0071D1C2  0F 57 C0                        xorps xmm0, xmm0
0071D1C5  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
0071D1C9  1B D2                           sbb edx, edx
0071D1CB  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
0071D1CF  83 E2 40                        and edx, 0x40
0071D1D2  48 C7 45 D0 30 00 00 00         mov qword ptr [rbp - 0x30], 0x30
0071D1DA  81 C2 00 02 00 00               add edx, 0x200
0071D1E0  89 5D EC                        mov dword ptr [rbp - 0x14], ebx
0071D1E3  89 55 E8                        mov dword ptr [rbp - 0x18], edx
0071D1E6  8D 47 48                        lea eax, [rdi + 0x48]
0071D1E9  48 8B 15 30 A1 8A 00            mov rdx, qword ptr [rip + 0x8aa130]
0071D1F0  45 33 C9                        xor r9d, r9d
0071D1F3  33 C9                           xor ecx, ecx
0071D1F5  48 89 5D 18                     mov qword ptr [rbp + 0x18], rbx
0071D1F9  48 89 5D 20                     mov qword ptr [rbp + 0x20], rbx
0071D1FD  48 89 5D D8                     mov qword ptr [rbp - 0x28], rbx
0071D201  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
0071D205  F3 0F 7F 45 F0                  movdqu xmmword ptr [rbp - 0x10], xmm0
0071D20A  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0071D20E  E8 CD DF 17 00                  call 0x14089b1e0
0071D213  85 C0                           test eax, eax
0071D215  78 7D                           js 0x14071d294
0071D217  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0071D21B  48 8D 45 20                     lea rax, [rbp + 0x20]
0071D21F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0071D224  44 8D 4B 01                     lea r9d, [rbx + 1]
0071D228  48 8D 45 18                     lea rax, [rbp + 0x18]
0071D22C  33 D2                           xor edx, edx
0071D22E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0071D233  44 8D 43 03                     lea r8d, [rbx + 3]
0071D237  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0071D23B  E8 60 C5 19 00                  call 0x1408b97a0
0071D240  85 C0                           test eax, eax
0071D242  78 50                           js 0x14071d294
0071D244  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
0071D248  33 D2                           xor edx, edx
0071D24A  E8 21 46 18 00                  call 0x1408a1870
0071D24F  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0071D253  BB 48 00 00 00                  mov ebx, 0x48
0071D258  33 D2                           xor edx, edx
0071D25A  4C 8D 04 3B                     lea r8, [rbx + rdi]
0071D25E  E8 DD 99 FA FF                  call 0x1406c6c40
0071D263  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
0071D267  66 03 FB                        add di, bx
0071D26A  66 C7 00 02 00                  mov word ptr [rax], 2
0071D26F  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
0071D273  66 89 78 02                     mov word ptr [rax + 2], di
0071D277  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0071D27B  48 8D 41 48                     lea rax, [rcx + 0x48]
0071D27F  48 89 41 08                     mov qword ptr [rcx + 8], rax
0071D283  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0071D287  48 83 C1 10                     add rcx, 0x10
0071D28B  E8 C0 AC D9 FF                  call 0x1404b7f50
0071D290  48 8B 5D 18                     mov rbx, qword ptr [rbp + 0x18]
0071D294  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
0071D29C  48 8B C3                        mov rax, rbx
0071D29F  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0071D2A3  49 8B 7B 28                     mov rdi, qword ptr [r11 + 0x28]
0071D2A7  49 8B E3                        mov rsp, r11
0071D2AA  5D                              pop rbp
0071D2AB  C3                              ret
0071D2AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoCreateController(int a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (128);
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 72) = v_stack_p10;
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rip + 7264276))));
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    a2 = (unsigned int)((a2) & (64));
    v_stack_m38 = 48;
    a2 = (unsigned int)((a2) + (512));
    v_stack_m1C = 0;
    v_stack_m20 = a2;
    a4 = 0;
    a1 = 0;
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    v_stack_m30 = 0;
    v_stack_m28 = 0;
    v_stack_m18 = v_xmm0;
    v_stack_m60 = (unsigned int)((unsigned int)(a1) + 72);
    result = ObCreateObjectEx(a1, *(unsigned __int64 *)(v_rip + 9085232), v_stack_m38, a4);
    if (sign_flag) goto loc_0071D294;
    v_stack_m58 = v_stack_p18;
    a2 = 0;
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = 0;
    result = ObInsertObjectEx(v_stack_p10, a2, v_rbx + 3, v_rbx + 1);
    v_rdi = (unsigned int)(a1);
    if (!(sign_flag)) {
        a1 = v_stack_p18;
        a2 = 0;
        result = ObCloseHandle(a1, a2, v_rbx + 3, v_rbx + 1);
        a1 = v_stack_p10;
        v_rbx = 72;
        a2 = 0;
        a3 = v_rbx + (unsigned int)(a1) * 1;
        result = memset(a1, a2, a3, v_rbx + 1);
        result = v_stack_p10;
        v_rdi = (unsigned __int16)(((unsigned int)(a1)) + ((unsigned __int16)(v_rbx)));
        *(unsigned __int16 *)(result) = 2;
        result = v_stack_p10;
        *(unsigned __int16 *)(result + 2) = (unsigned __int16)(v_rdi);
        a1 = v_stack_p10;
        result = a1 + 72;
        *(unsigned __int64 *)(a1 + 8) = result;
        a1 = v_stack_p10;
        a1 = (a1) + (16);
        result = KeInitializeDeviceQueue(a1, a2, a3, v_rbx + 1);
        v_rbx = v_stack_p10;
    }
    return v_rbx;
}
```

## 5. (Beta) C Style

```c
int64_t IoCreateController(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (128);
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0x48) = v_stack_p10;
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_rip + 0x6ED814))));
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    Arg2 = (uint32_t)((Arg2) & (64));
    v_stack_m38 = 48;
    Arg2 = (uint32_t)((Arg2) + (512));
    v_stack_m1C = 0;
    v_stack_m20 = Arg2;
    Arg4 = 0;
    Arg1 = 0;
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    v_stack_m30 = 0;
    v_stack_m28 = 0;
    v_stack_m18 = v_xmm0;
    v_stack_m60 = (uint32_t)((uint32_t)(Arg1) + 72);
    result = ObCreateObjectEx(Arg1, *(uint64_t *)(v_rip + 0x8AA130), v_stack_m38, Arg4);
    if (sign_flag) goto loc_0071D294;
    v_stack_m58 = v_stack_p18;
    Arg2 = 0;
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = 0;
    result = ObInsertObjectEx(v_stack_p10, Arg2, local_rbx + 3, local_rbx + 1);
    local_rdi = (uint32_t)(Arg1);
    if (!(sign_flag)) {
        Arg1 = v_stack_p18;
        Arg2 = 0;
        result = ObCloseHandle(Arg1, Arg2, local_rbx + 3, local_rbx + 1);
        Arg1 = v_stack_p10;
        local_rbx = 72;
        Arg2 = 0;
        Arg3 = local_rbx + (uint32_t)(Arg1) * 1;
        result = memset(Arg1, Arg2, Arg3, local_rbx + 1);
        result = v_stack_p10;
        local_rdi = (uint16_t)(((uint32_t)(Arg1)) + ((uint16_t)(local_rbx)));
        *(uint16_t *)(result) = 2;
        result = v_stack_p10;
        *(uint16_t *)(result + 0x2) = (uint16_t)(local_rdi);
        Arg1 = v_stack_p10;
        result = Arg1 + 72;
        *(uint64_t *)(arg1 + 0x8) = result;
        Arg1 = v_stack_p10;
        Arg1 = (Arg1) + (16);
        result = KeInitializeDeviceQueue(Arg1, Arg2, Arg3, local_rbx + 1);
        local_rbx = v_stack_p10;
    }
    return local_rbx;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x48` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0071D190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0071D190[BB_0071D190]
  bb_0071D217[BB_0071D217]
  bb_0071D244[BB_0071D244]
  bb_0071D294[BB_0071D294]
  bb_0071D2AC[BB_0071D2AC]
  bb_0071D190 -->|branch| bb_0071D294
  bb_0071D190 -->|fallthrough| bb_0071D217
  bb_0071D217 -->|branch| bb_0071D294
  bb_0071D217 -->|fallthrough| bb_0071D244
  bb_0071D244 -->|flow| bb_0071D294
```
