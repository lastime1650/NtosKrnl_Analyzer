# PopDiagTraceSessionDisplayStateChange

- RVA: `0x004B7C00`–`0x004B7CDD` (길이 `221` bytes)
- VA: `0x00000001404B7C00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BAAF0`
- 디코드: `53`개 명령, `221/221` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x004B7C52` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004B7CBA` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004B7CC6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtPowerInformation](../../page/95/NtPowerInformation_function_00955D80.md) at `0x00956E3C`
- [PopPowerInformationInternal](../../page/A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8BD0F`

### Static image references
- `0x004B7C1D` → RVA `0x00E0A740` (`.data`; read)
- `0x004B7C2D` → RVA `0x0001C7A0` (`.rdata`; read)
- `0x004B7C34` → RVA `0x0001C790` (`.rdata`; read)
- `0x004B7C3F` → RVA `0x00E67858` (`.data`; read)
- `0x004B7C48` → RVA `0x00F0B408` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B7C00  48 8B C4                        mov rax, rsp
004B7C03  48 89 58 08                     mov qword ptr [rax + 8], rbx
004B7C07  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
004B7C0B  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
004B7C0F  89 50 10                        mov dword ptr [rax + 0x10], edx
004B7C12  55                              push rbp
004B7C13  48 8B EC                        mov rbp, rsp
004B7C16  48 81 EC 80 00 00 00            sub rsp, 0x80
004B7C1D  48 8B 05 1C 2B 95 00            mov rax, qword ptr [rip + 0x952b1c]
004B7C24  48 33 C4                        xor rax, rsp
004B7C27  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
004B7C2B  84 C9                           test cl, cl
004B7C2D  48 8D 05 6C 4B B6 FF            lea rax, [rip - 0x49b494]
004B7C34  48 8D 1D 55 4B B6 FF            lea rbx, [rip - 0x49b4ab]
004B7C3B  48 0F 44 D8                     cmove rbx, rax
004B7C3F  80 3D 12 FC 9A 00 00            cmp byte ptr [rip + 0x9afc12], 0
004B7C46  74 77                           je 0x1404b7cbf
004B7C48  48 8B 0D B9 37 A5 00            mov rcx, qword ptr [rip + 0xa537b9]
004B7C4F  48 8B D3                        mov rdx, rbx
004B7C52  E8 F9 A7 ED FF                  call 0x140392450
004B7C57  84 C0                           test al, al
004B7C59  74 64                           je 0x1404b7cbf
004B7C5B  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
004B7C5F  48 8D 45 18                     lea rax, [rbp + 0x18]
004B7C63  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
004B7C67  B9 04 00 00 00                  mov ecx, 4
004B7C6C  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
004B7C70  45 33 C9                        xor r9d, r9d
004B7C73  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
004B7C77  45 33 C0                        xor r8d, r8d
004B7C7A  48 8D 45 20                     lea rax, [rbp + 0x20]
004B7C7E  89 4D C8                        mov dword ptr [rbp - 0x38], ecx
004B7C81  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
004B7C85  48 8B D3                        mov rdx, rbx
004B7C88  48 8D 45 28                     lea rax, [rbp + 0x28]
004B7C8C  89 4D D8                        mov dword ptr [rbp - 0x28], ecx
004B7C8F  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
004B7C93  48 8D 45 C0                     lea rax, [rbp - 0x40]
004B7C97  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004B7C9C  C7 44 24 30 03 00 00 00         mov dword ptr [rsp + 0x30], 3
004B7CA4  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
004B7CAA  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004B7CB0  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
004B7CB3  48 8B 0D 4E 37 A5 00            mov rcx, qword ptr [rip + 0xa5374e]
004B7CBA  E8 11 74 DA FF                  call 0x14025f0d0
004B7CBF  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
004B7CC3  48 33 CC                        xor rcx, rsp
004B7CC6  E8 75 49 1F 00                  call 0x1406ac640
004B7CCB  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
004B7CD3  48 81 C4 80 00 00 00            add rsp, 0x80
004B7CDA  5D                              pop rbp
004B7CDB  C3                              ret
004B7CDC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceSessionDisplayStateChange(unsigned __int8 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 9775900)) ^ (v_rsp);
    v_stack_m18 = result;
    v_rbx = v_rip - 4830379;
    if (a1 == 0) { v_rbx = v_rip - 4830356; }
    if ((*(unsigned __int8 *)(v_rip + 10157074)) == 0) goto loc_004B7CBF;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10827705), v_rbx, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p10;
        a1 = 4;
        a4 = 0;
        v_stack_m48 = result;
        a3 = 0;
        result = v_stack_p18;
        v_stack_m40 = a1;
        v_stack_m38 = result;
        a2 = v_rbx;
        result = v_stack_p20;
        v_stack_m30 = a1;
        v_stack_m28 = result;
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m20 = a1;
        a1 = *(unsigned __int64 *)(v_rip + 10827598);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceSessionDisplayStateChange(uint8_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x952B1C)) ^ (local_rsp);
    v_stack_m18 = result;
    local_rbx = v_rip - 4830379;
    if (Arg1 == 0) { local_rbx = v_rip - 4830356; }
    if ((*(uint8_t *)(v_rip + 0x9AFC12)) == 0) goto loc_004B7CBF;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA537B9), local_rbx, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p10;
        Arg1 = 4;
        Arg4 = 0;
        v_stack_m48 = result;
        Arg3 = 0;
        result = v_stack_p18;
        v_stack_m40 = Arg1;
        v_stack_m38 = result;
        Arg2 = local_rbx;
        result = v_stack_p20;
        v_stack_m30 = Arg1;
        v_stack_m28 = result;
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m20 = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0xA5374E);
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B7C00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B7C00[BB_004B7C00]
  bb_004B7C48[BB_004B7C48]
  bb_004B7C5B[BB_004B7C5B]
  bb_004B7CBF[BB_004B7CBF]
  bb_004B7CDC[BB_004B7CDC]
  bb_004B7C00 -->|branch| bb_004B7CBF
  bb_004B7C00 -->|fallthrough| bb_004B7C48
  bb_004B7C48 -->|branch| bb_004B7CBF
  bb_004B7C48 -->|fallthrough| bb_004B7C5B
  bb_004B7C5B -->|flow| bb_004B7CBF
```
