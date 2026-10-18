# PpLastGoodDeleteFilesCallback

- RVA: `0x0072BD10`–`0x0072BDDA` (길이 `202` bytes)
- VA: `0x000000014072BD10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C866C`
- 디코드: `52`개 명령, `202/202` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0072BD3E` → [IopFileUtilClearAttributes](../73/IopFileUtilClearAttributes_function_0073FA1C.md) (function, `0x0073FA1C`)
- `0x0072BD90` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (function, `0x006AD730`)
- `0x0072BDB7` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (function, `0x006AD5B0`)
- `0x0072BDC0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0072BD90` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (`PAGE` → `.text`)
  - `0x0072BDB7` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (`PAGE` → `.text`)
  - `0x0072BDC0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0072BD10  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0072BD15  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0072BD1A  55                              push rbp
0072BD1B  48 8B EC                        mov rbp, rsp
0072BD1E  48 83 EC 70                     sub rsp, 0x70
0072BD22  33 C0                           xor eax, eax
0072BD24  0F 57 C0                        xorps xmm0, xmm0
0072BD27  21 45 EC                        and dword ptr [rbp - 0x14], eax
0072BD2A  41 8B F8                        mov edi, r8d
0072BD2D  48 21 45 10                     and qword ptr [rbp + 0x10], rax
0072BD31  48 8B D9                        mov rbx, rcx
0072BD34  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
0072BD37  21 45 D4                        and dword ptr [rbp - 0x2c], eax
0072BD3A  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0072BD3E  E8 D9 3C 01 00                  call 0x14073fa1c
0072BD43  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
0072BD48  4C 8D 4D C0                     lea r9, [rbp - 0x40]
0072BD4C  0F 57 C0                        xorps xmm0, xmm0
0072BD4F  C7 45 D0 30 00 00 00            mov dword ptr [rbp - 0x30], 0x30
0072BD56  40 80 E7 10                     and dil, 0x10
0072BD5A  C7 45 E8 40 00 00 00            mov dword ptr [rbp - 0x18], 0x40
0072BD61  40 F6 DF                        neg dil
0072BD64  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
0072BD68  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0072BD6C  BA 80 00 01 00                  mov edx, 0x10080
0072BD71  1B C0                           sbb eax, eax
0072BD73  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0072BD77  83 E0 C1                        and eax, 0xffffffc1
0072BD7A  05 40 40 20 00                  add eax, 0x204040
0072BD7F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0072BD83  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
0072BD8B  F3 0F 7F 45 F0                  movdqu xmmword ptr [rbp - 0x10], xmm0
0072BD90  E8 9B 19 F8 FF                  call 0x1406ad730
0072BD95  85 C0                           test eax, eax
0072BD97  78 2E                           js 0x14072bdc7
0072BD99  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0072BD9D  4C 8D 45 20                     lea r8, [rbp + 0x20]
0072BDA1  41 B9 01 00 00 00               mov r9d, 1
0072BDA7  C6 45 20 01                     mov byte ptr [rbp + 0x20], 1
0072BDAB  48 8D 55 C0                     lea rdx, [rbp - 0x40]
0072BDAF  C7 44 24 20 0D 00 00 00         mov dword ptr [rsp + 0x20], 0xd
0072BDB7  E8 F4 17 F8 FF                  call 0x1406ad5b0
0072BDBC  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0072BDC0  E8 EB 14 F8 FF                  call 0x1406ad2b0
0072BDC5  33 C0                           xor eax, eax
0072BDC7  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0072BDCC  49 8B 5B 18                     mov rbx, qword ptr [r11 + 0x18]
0072BDD0  49 8B 7B 28                     mov rdi, qword ptr [r11 + 0x28]
0072BDD4  49 8B E3                        mov rsp, r11
0072BDD7  5D                              pop rbp
0072BDD8  C3                              ret
0072BDD9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpLastGoodDeleteFilesCallback(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m34 = 0;
    v_stack_m48 = v_xmm0;
    result = IopFileUtilClearAttributes(a1, a2, a3, a4);
    v_stack_m38 = 48;
    v_rdi = (unsigned __int8)(((unsigned int)(a3)) & (16));
    v_stack_m20 = 64;
    v_rdi = (unsigned __int8)(-(v_rdi));
    v_stack_m28 = a1;
    result = (unsigned int)((result) & (0xFFFFFFC1ULL));
    result = (unsigned int)((result) + (0x204040ULL));
    v_stack_m50 = (unsigned int)(result);
    v_stack_m58 = 7;
    v_stack_m18 = v_xmm0;
    result = ZwOpenFile(v_stack_p8, (unsigned int)(0x10080ULL), v_stack_m38, v_stack_m48);
    if (!(sign_flag)) {
        a1 = v_stack_p8;
        a3 = v_stack_p18;
        a4 = 1;
        v_stack_p18 = 1;
        a2 = v_stack_m48;
        v_stack_m58 = 13;
        result = ZwSetInformationFile(a1, a2, a3, a4);
        a1 = v_stack_p8;
        result = ZwClose(a1, a2, a3, a4);
        result = 0;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpLastGoodDeleteFilesCallback(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m34 = 0;
    v_stack_m48 = v_xmm0;
    result = IopFileUtilClearAttributes(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = 48;
    local_rdi = (uint8_t)(((uint32_t)(Arg3)) & (16));
    v_stack_m20 = 64;
    local_rdi = (uint8_t)(-(local_rdi));
    v_stack_m28 = Arg1;
    result = (uint32_t)((result) & (0xFFFFFFC1ULL));
    result = (uint32_t)((result) + (0x204040ULL));
    v_stack_m50 = (uint32_t)(result);
    v_stack_m58 = 7;
    v_stack_m18 = v_xmm0;
    result = ZwOpenFile(v_stack_p8, (uint32_t)(0x10080ULL), v_stack_m38, v_stack_m48);
    if (!(sign_flag)) {
        Arg1 = v_stack_p8;
        Arg3 = v_stack_p18;
        a4 = 1;
        v_stack_p18 = 1;
        Arg2 = v_stack_m48;
        v_stack_m58 = 13;
        result = ZwSetInformationFile(Arg1, Arg2, Arg3, a4);
        Arg1 = v_stack_p8;
        result = ZwClose(Arg1, Arg2, Arg3, a4);
        result = 0;
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0072BD10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0072BD10[BB_0072BD10]
  bb_0072BD99[BB_0072BD99]
  bb_0072BDC7[BB_0072BDC7]
  bb_0072BDD9[BB_0072BDD9]
  bb_0072BD10 -->|branch| bb_0072BDC7
  bb_0072BD10 -->|fallthrough| bb_0072BD99
  bb_0072BD99 -->|flow| bb_0072BDC7
```
