# EtwTraceMdlAllocationEvent

- RVA: `0x003E95FC`–`0x003E96E2` (길이 `230` bytes)
- VA: `0x00000001403E95FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00095848`
- 디코드: `60`개 명령, `230/230` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x003E9637` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x003E9647` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003E965F` → [EtwpGetDurationSince](EtwpGetDurationSince_function_003EA7D4.md) (function, `0x003EA7D4`)
- `0x003E96D8` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- [MiAllocatePagesForMdl](MiAllocatePagesForMdl_function_003EABEC.md) at `0x003EAE71`

### Static image references
- `0x003E960F` → RVA `0x00E0A740` (`.data`; read)
- `0x003E9623` → RVA `0x00EFF848` (`.data`; read)
- `0x003E962A` → RVA `0x00012CE8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E95FC  40 55                           push rbp
003E95FE  53                              push rbx
003E95FF  56                              push rsi
003E9600  57                              push rdi
003E9601  41 56                           push r14
003E9603  48 8D 6C 24 F1                  lea rbp, [rsp - 0xf]
003E9608  48 81 EC A0 00 00 00            sub rsp, 0xa0
003E960F  48 8B 05 2A 11 A2 00            mov rax, qword ptr [rip + 0xa2112a]
003E9616  48 33 C4                        xor rax, rsp
003E9619  48 89 45 FF                     mov qword ptr [rbp - 1], rax
003E961D  48 8B DA                        mov rbx, rdx
003E9620  4C 8B F1                        mov r14, rcx
003E9623  48 8B 0D 1E 62 B1 00            mov rcx, qword ptr [rip + 0xb1621e]
003E962A  48 8D 15 B7 96 C2 FF            lea rdx, [rip - 0x3d6949]
003E9631  49 8B F1                        mov rsi, r9
003E9634  49 8B F8                        mov rdi, r8
003E9637  E8 14 8E FA FF                  call 0x140392450
003E963C  84 C0                           test al, al
003E963E  75 1B                           jne 0x1403e965b
003E9640  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
003E9644  48 33 CC                        xor rcx, rsp
003E9647  E8 F4 2F 2C 00                  call 0x1406ac640
003E964C  48 81 C4 A0 00 00 00            add rsp, 0xa0
003E9653  41 5E                           pop r14
003E9655  5F                              pop rdi
003E9656  5E                              pop rsi
003E9657  5B                              pop rbx
003E9658  5D                              pop rbp
003E9659  C3                              ret
003E965A  CC                              int3
003E965B  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
003E965F  E8 70 11 00 00                  call 0x1403ea7d4
003E9664  83 65 FB 00                     and dword ptr [rbp - 5], 0
003E9668  48 8D 15 79 96 C2 FF            lea rdx, [rip - 0x3d6987]
003E966F  48 8B 0D D2 61 B1 00            mov rcx, qword ptr [rip + 0xb161d2]
003E9676  41 B9 01 00 00 00               mov r9d, 1
003E967C  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
003E9680  45 33 C0                        xor r8d, r8d
003E9683  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
003E9686  89 45 DF                        mov dword ptr [rbp - 0x21], eax
003E9689  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
003E968C  89 45 E3                        mov dword ptr [rbp - 0x1d], eax
003E968F  48 8B 45 5F                     mov rax, qword ptr [rbp + 0x5f]
003E9693  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
003E9697  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
003E969B  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
003E969F  48 8D 45 AF                     lea rax, [rbp - 0x51]
003E96A3  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
003E96A7  48 8D 45 EF                     lea rax, [rbp - 0x11]
003E96AB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003E96B0  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
003E96B5  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
003E96BB  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
003E96C1  4C 89 75 D7                     mov qword ptr [rbp - 0x29], r14
003E96C5  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
003E96C9  48 89 7D C7                     mov qword ptr [rbp - 0x39], rdi
003E96CD  48 89 75 CF                     mov qword ptr [rbp - 0x31], rsi
003E96D1  C7 45 F7 40 00 00 00            mov dword ptr [rbp - 9], 0x40
003E96D8  E8 F3 59 E7 FF                  call 0x14025f0d0
003E96DD  E9 5E FF FF FF                  jmp 0x1403e9640
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceMdlAllocationEvent(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m37;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 10621226)) ^ (v_rsp);
    v_stack_m38 = result;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 11624990), v_rip - 4024649, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_003E965B;
loc_003E9640:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 4024649, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
loc_003E965B:
    result = EtwpGetDurationSince(a9, v_rip - 4024649, a3, a4);
    v_stack_m88 = result;
    a3 = 0;
    v_stack_m58 = (unsigned int)((unsigned int)(a6));
    v_stack_m54 = (unsigned int)((unsigned int)(a7));
    v_stack_m80 = a5;
    v_stack_m50 = a8;
    v_stack_m48 = v_stack_m88;
    v_stack_p38 = v_stack_m48;
    v_stack_p30 = 1;
    v_stack_m60 = a1;
    v_stack_m78 = a2;
    v_stack_m70 = 0;
    v_stack_m68 = a4;
    v_stack_m40 = 64;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 11624914), v_rip - 4024711, a3, 1);
    goto loc_003E9640;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceMdlAllocationEvent(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m37;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0xA2112A)) ^ (local_rsp);
    v_stack_m38 = result;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xB1621E), v_rip - 4024649, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_003E965B;
loc_003E9640:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 4024649, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
loc_003E965B:
    result = EtwpGetDurationSince(Arg9, v_rip - 4024649, Arg3, Arg4);
    v_stack_m88 = result;
    Arg3 = 0;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m54 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m80 = Arg5;
    v_stack_m50 = Arg8;
    v_stack_m48 = v_stack_m88;
    v_stack_p38 = v_stack_m48;
    v_stack_p30 = 1;
    v_stack_m60 = Arg1;
    v_stack_m78 = Arg2;
    v_stack_m70 = 0;
    v_stack_m68 = Arg4;
    v_stack_m40 = 64;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xB161D2), v_rip - 4024711, Arg3, 1);
    goto loc_003E9640;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E95FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E95FC[BB_003E95FC]
  bb_003E9640[BB_003E9640]
  bb_003E965A[BB_003E965A]
  bb_003E965B[BB_003E965B]
  bb_003E95FC -->|branch| bb_003E965B
  bb_003E95FC -->|fallthrough| bb_003E9640
  bb_003E965A -->|flow| bb_003E965B
  bb_003E965B -->|branch| bb_003E9640
```
