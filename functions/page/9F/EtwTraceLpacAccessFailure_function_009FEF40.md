# EtwTraceLpacAccessFailure

- RVA: `0x009FEF40`–`0x009FEFD0` (길이 `144` bytes)
- VA: `0x00000001409FEF40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A76F8`
- 디코드: `34`개 명령, `144/144` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009FEF6D` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (function, `0x0037DA40`)
- `0x009FEFB8` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x009FEFC4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SepLogLpacAccessFailure](../../text/41/SepLogLpacAccessFailure_function_0041E8A0.md) at `0x0041E8F5`

### Static image references
- `0x009FEF4C` → RVA `0x00E0A740` (`.data`; read)
- `0x009FEF5F` → RVA `0x00EFF820` (`.data`; read)
- `0x009FEF7E` → RVA `0x00014A20` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009FEF6D` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (`PAGE` → `.text`)
  - `0x009FEFB8` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x009FEFC4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009FEF40  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
009FEF44  55                              push rbp
009FEF45  48 8B EC                        mov rbp, rsp
009FEF48  48 83 EC 60                     sub rsp, 0x60
009FEF4C  48 8B 05 ED B7 40 00            mov rax, qword ptr [rip + 0x40b7ed]
009FEF53  48 33 C4                        xor rax, rsp
009FEF56  48 89 45 F8                     mov qword ptr [rbp - 8], rax
009FEF5A  48 83 65 D0 00                  and qword ptr [rbp - 0x30], 0
009FEF5F  48 83 3D B9 08 50 00 00         cmp qword ptr [rip + 0x5008b9], 0
009FEF67  74 54                           je 0x1409fefbd
009FEF69  48 8D 4D D0                     lea rcx, [rbp - 0x30]
009FEF6D  E8 CE EA 97 FF                  call 0x14037da40
009FEF72  83 65 E4 00                     and dword ptr [rbp - 0x1c], 0
009FEF76  48 8D 45 D0                     lea rax, [rbp - 0x30]
009FEF7A  83 65 F4 00                     and dword ptr [rbp - 0xc], 0
009FEF7E  48 8D 15 9B 5A 61 FF            lea rdx, [rip - 0x9ea565]
009FEF85  48 8B 0D 94 08 50 00            mov rcx, qword ptr [rip + 0x500894]
009FEF8C  41 B9 02 00 00 00               mov r9d, 2
009FEF92  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
009FEF96  45 33 C0                        xor r8d, r8d
009FEF99  48 8D 45 10                     lea rax, [rbp + 0x10]
009FEF9D  C7 45 E0 08 00 00 00            mov dword ptr [rbp - 0x20], 8
009FEFA4  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
009FEFA8  48 8D 45 D8                     lea rax, [rbp - 0x28]
009FEFAC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009FEFB1  C7 45 F0 04 00 00 00            mov dword ptr [rbp - 0x10], 4
009FEFB8  E8 63 D7 A1 FF                  call 0x14041c720
009FEFBD  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
009FEFC1  48 33 CC                        xor rcx, rsp
009FEFC4  E8 77 D6 CA FF                  call 0x1406ac640
009FEFC9  48 83 C4 60                     add rsp, 0x60
009FEFCD  5D                              pop rbp
009FEFCE  C3                              ret
009FEFCF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceLpacAccessFailure(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 4241389)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned __int64 *)(v_rip + 5245113)) != 0) {
        a1 = v_stack_m38;
        result = KeQuerySystemTimePrecise(a1, a2, a3, a4);
        result = v_stack_m38;
        a2 = v_rip - 10397029;
        a1 = *(unsigned __int64 *)(v_rip + 5245076);
        a4 = 2;
        v_stack_m30 = result;
        a3 = 0;
        result = v_stack_p8;
        v_stack_m28 = 8;
        v_stack_m20 = result;
        result = v_stack_m30;
        v_stack_m48 = result;
        v_stack_m18 = 4;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceLpacAccessFailure(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x40B7ED)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint64_t *)(v_rip + 0x5008B9)) != 0) {
        Arg1 = v_stack_m38;
        result = KeQuerySystemTimePrecise(Arg1, Arg2, Arg3, a4);
        result = v_stack_m38;
        Arg2 = v_rip - 10397029;
        Arg1 = *(uint64_t *)(v_rip + 0x500894);
        a4 = 2;
        v_stack_m30 = result;
        Arg3 = 0;
        result = v_stack_p8;
        v_stack_m28 = 8;
        v_stack_m20 = result;
        result = v_stack_m30;
        v_stack_m48 = result;
        v_stack_m18 = 4;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009FEF40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009FEF40[BB_009FEF40]
  bb_009FEF69[BB_009FEF69]
  bb_009FEFBD[BB_009FEFBD]
  bb_009FEFCF[BB_009FEFCF]
  bb_009FEF40 -->|branch| bb_009FEFBD
  bb_009FEF40 -->|fallthrough| bb_009FEF69
  bb_009FEF69 -->|flow| bb_009FEFBD
```
