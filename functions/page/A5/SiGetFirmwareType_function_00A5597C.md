# SiGetFirmwareType

- RVA: `0x00A5597C`–`0x00A559DD` (길이 `97` bytes)
- VA: `0x0000000140A5597C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000606C0`
- 디코드: `27`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A559B2` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)
- `0x00A559D1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SiGetSystemDeviceName](SiGetSystemDeviceName_function_00A558B8.md) at `0x00A558E4`

### Static image references
- `0x00A55982` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A559B2` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (`PAGE` → `.text`)
  - `0x00A559D1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A5597C  40 53                           push rbx
00A5597E  48 83 EC 50                     sub rsp, 0x50
00A55982  48 8B 05 B7 4D 3B 00            mov rax, qword ptr [rip + 0x3b4db7]
00A55989  48 33 C4                        xor rax, rsp
00A5598C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A55991  0F 57 C0                        xorps xmm0, xmm0
00A55994  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00A55999  BB 01 00 00 00                  mov ebx, 1
00A5599E  45 33 C9                        xor r9d, r9d
00A559A1  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00A559A6  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
00A559AB  44 8D 43 1F                     lea r8d, [rbx + 0x1f]
00A559AF  8D 4B 59                        lea ecx, [rbx + 0x59]
00A559B2  E8 D9 7D C5 FF                  call 0x1406ad790
00A559B7  85 C0                           test eax, eax
00A559B9  78 0C                           js 0x140a559c7
00A559BB  33 DB                           xor ebx, ebx
00A559BD  83 7C 24 30 03                  cmp dword ptr [rsp + 0x30], 3
00A559C2  0F 4C 5C 24 30                  cmovl ebx, dword ptr [rsp + 0x30]
00A559C7  8B C3                           mov eax, ebx
00A559C9  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00A559CE  48 33 CC                        xor rcx, rsp
00A559D1  E8 6A 6C C5 FF                  call 0x1406ac640
00A559D6  48 83 C4 50                     add rsp, 0x50
00A559DA  5B                              pop rbx
00A559DB  C3                              ret
00A559DC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SiGetFirmwareType(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (80);
    result = (*(unsigned __int64 *)(v_rip + 3886519)) ^ (v_rsp);
    v_stack_m18 = result;
    a4 = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    result = ZwQuerySystemInformation(1 + 89, v_stack_m38, 1 + 31, a4);
    v_rbx = 1;
    if (!(sign_flag)) {
        v_rbx = 0;
        if (v_stack_m28 < 3) { v_rbx = v_stack_m28; }
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m38, 1 + 31, a4);
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SiGetFirmwareType(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (80);
    result = (*(uint64_t *)(v_rip + 0x3B4DB7)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg4 = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    result = ZwQuerySystemInformation(1 + 89, v_stack_m38, 1 + 31, Arg4);
    local_rbx = 1;
    if (!(sign_flag)) {
        local_rbx = 0;
        if (v_stack_m28 < 3) { local_rbx = v_stack_m28; }
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m38, 1 + 31, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A5597C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A5597C[BB_00A5597C]
  bb_00A559BB[BB_00A559BB]
  bb_00A559C7[BB_00A559C7]
  bb_00A559DC[BB_00A559DC]
  bb_00A5597C -->|branch| bb_00A559C7
  bb_00A5597C -->|fallthrough| bb_00A559BB
  bb_00A559BB -->|flow| bb_00A559C7
```
