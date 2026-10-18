# CmpTraceHiveMountStop

- RVA: `0x009B8038`–`0x009B80C1` (길이 `137` bytes)
- VA: `0x00000001409B8038`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CABC`
- 디코드: `30`개 명령, `137/137` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009B8068` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009B8079` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009B80BA` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [HvHiveStartFileBacked](HvHiveStartFileBacked_function_009B7E20.md) at `0x009B7F34`

### Static image references
- `0x009B8040` → RVA `0x00E0A740` (`.data`; read)
- `0x009B804F` → RVA `0x00013C80` (`.rdata`; read)
- `0x009B8056` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009B8068` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009B8079` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009B80BA` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009B8038  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
009B803C  48 83 EC 68                     sub rsp, 0x68
009B8040  48 8B 05 F9 26 45 00            mov rax, qword ptr [rip + 0x4526f9]
009B8047  48 33 C4                        xor rax, rsp
009B804A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009B804F  0F 10 05 2A BC 65 FF            movups xmm0, xmmword ptr [rip - 0x9a43d6]
009B8056  48 8B 0D BB FF 61 00            mov rcx, qword ptr [rip + 0x61ffbb]
009B805D  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
009B8062  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
009B8068  E8 E3 A3 9D FF                  call 0x140392450
009B806D  84 C0                           test al, al
009B806F  75 13                           jne 0x1409b8084
009B8071  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009B8076  48 33 CC                        xor rcx, rsp
009B8079  E8 C2 45 CF FF                  call 0x1406ac640
009B807E  48 83 C4 68                     add rsp, 0x68
009B8082  C3                              ret
009B8083  CC                              int3
009B8084  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
009B8089  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009B808E  48 8B 0D 83 FF 61 00            mov rcx, qword ptr [rip + 0x61ff83]
009B8095  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
009B809A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009B809F  41 B9 01 00 00 00               mov r9d, 1
009B80A5  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009B80AA  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
009B80B2  45 33 C0                        xor r8d, r8d
009B80B5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009B80BA  E8 61 46 A6 FF                  call 0x14041c720
009B80BF  EB B0                           jmp 0x1409b8071
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveMountStop(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 4531961)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m38 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6422459), v_stack_m38, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009B8084;
loc_009B8071:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m38, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
loc_009B8084:
    v_stack_p40 = v_stack_p70;
    v_stack_p48 = 4;
    a3 = 0;
    v_stack_p20 = v_stack_p40;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 6422403), v_stack_p30, a3, 1);
    goto loc_009B8071;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveMountStop(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m38;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p70;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x4526F9)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m38 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x61FFBB), v_stack_m38, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_009B8084;
loc_009B8071:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m38, Arg3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
loc_009B8084:
    v_stack_p40 = v_stack_p70;
    v_stack_p48 = 4;
    Arg3 = 0;
    v_stack_p20 = v_stack_p40;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x61FF83), v_stack_p30, Arg3, 1);
    goto loc_009B8071;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B8038&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009B8038[BB_009B8038]
  bb_009B8071[BB_009B8071]
  bb_009B8083[BB_009B8083]
  bb_009B8084[BB_009B8084]
  bb_009B8038 -->|branch| bb_009B8084
  bb_009B8038 -->|fallthrough| bb_009B8071
  bb_009B8083 -->|flow| bb_009B8084
  bb_009B8084 -->|branch| bb_009B8071
```
