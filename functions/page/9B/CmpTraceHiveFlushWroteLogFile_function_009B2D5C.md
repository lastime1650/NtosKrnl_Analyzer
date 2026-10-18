# CmpTraceHiveFlushWroteLogFile

- RVA: `0x009B2D5C`–`0x009B2DF5` (길이 `153` bytes)
- VA: `0x00000001409B2D5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009E41C`
- 디코드: `39`개 명령, `153/153` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009B2D94` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009B2DA4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009B2DEE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [HvWriteLogFile](HvWriteLogFile_function_009B28E4.md) at `0x009B29B3`

### Static image references
- `0x009B2D68` → RVA `0x00E0A740` (`.data`; read)
- `0x009B2D76` → RVA `0x00013C20` (`.rdata`; read)
- `0x009B2D7D` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009B2D94` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009B2DA4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009B2DEE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009B2D5C  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
009B2D60  55                              push rbp
009B2D61  48 8B EC                        mov rbp, rsp
009B2D64  48 83 EC 70                     sub rsp, 0x70
009B2D68  48 8B 05 D1 79 45 00            mov rax, qword ptr [rip + 0x4579d1]
009B2D6F  48 33 C4                        xor rax, rsp
009B2D72  48 89 45 F8                     mov qword ptr [rbp - 8], rax
009B2D76  0F 10 05 A3 0E 66 FF            movups xmm0, xmmword ptr [rip - 0x99f15d]
009B2D7D  48 8B 0D 94 52 62 00            mov rcx, qword ptr [rip + 0x625294]
009B2D84  48 8D 55 C8                     lea rdx, [rbp - 0x38]
009B2D88  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
009B2D8F  F3 0F 7F 45 C8                  movdqu xmmword ptr [rbp - 0x38], xmm0
009B2D94  E8 B7 F6 9D FF                  call 0x140392450
009B2D99  84 C0                           test al, al
009B2D9B  75 13                           jne 0x1409b2db0
009B2D9D  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
009B2DA1  48 33 CC                        xor rcx, rsp
009B2DA4  E8 97 98 CF FF                  call 0x1406ac640
009B2DA9  48 83 C4 70                     add rsp, 0x70
009B2DAD  5D                              pop rbp
009B2DAE  C3                              ret
009B2DAF  CC                              int3
009B2DB0  83 65 E4 00                     and dword ptr [rbp - 0x1c], 0
009B2DB4  48 8D 45 C0                     lea rax, [rbp - 0x40]
009B2DB8  83 65 F4 00                     and dword ptr [rbp - 0xc], 0
009B2DBC  48 8D 55 C8                     lea rdx, [rbp - 0x38]
009B2DC0  B9 04 00 00 00                  mov ecx, 4
009B2DC5  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
009B2DC9  48 8D 45 18                     lea rax, [rbp + 0x18]
009B2DCD  89 4D E0                        mov dword ptr [rbp - 0x20], ecx
009B2DD0  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
009B2DD4  45 33 C0                        xor r8d, r8d
009B2DD7  48 8D 45 D8                     lea rax, [rbp - 0x28]
009B2DDB  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
009B2DDE  44 8D 49 FE                     lea r9d, [rcx - 2]
009B2DE2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009B2DE7  48 8B 0D 2A 52 62 00            mov rcx, qword ptr [rip + 0x62522a]
009B2DEE  E8 2D 99 A6 FF                  call 0x14041c720
009B2DF3  EB A8                           jmp 0x1409b2d9d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveFlushWroteLogFile(__int64 a1, int a2, int a3)
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
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 4553169)) ^ (v_rsp);
    v_stack_m10 = result;
    v_stack_m48 = 1;
    v_stack_m40 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6443668), v_stack_m40, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009B2DB0;
loc_009B2D9D:
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m40, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
loc_009B2DB0:
    v_stack_m30 = v_stack_m48;
    v_stack_m28 = 4;
    v_stack_m20 = v_stack_p10;
    a3 = 0;
    v_stack_m18 = 4;
    v_stack_p20 = v_stack_m30;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 6443562), v_stack_m40, a3, 4 - 2);
    goto loc_009B2D9D;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveFlushWroteLogFile(int64_t Arg1, int32_t Arg2, int32_t Arg3)
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
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p20;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x4579D1)) ^ (local_rsp);
    v_stack_m10 = result;
    v_stack_m48 = 1;
    v_stack_m40 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x625294), v_stack_m40, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_009B2DB0;
loc_009B2D9D:
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m40, Arg3, a4);
    local_rsp = (local_rsp) + (112);
    return result;
loc_009B2DB0:
    v_stack_m30 = v_stack_m48;
    v_stack_m28 = 4;
    v_stack_m20 = v_stack_p10;
    Arg3 = 0;
    v_stack_m18 = 4;
    v_stack_p20 = v_stack_m30;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x62522A), v_stack_m40, Arg3, 4 - 2);
    goto loc_009B2D9D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B2D5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009B2D5C[BB_009B2D5C]
  bb_009B2D9D[BB_009B2D9D]
  bb_009B2DAF[BB_009B2DAF]
  bb_009B2DB0[BB_009B2DB0]
  bb_009B2D5C -->|branch| bb_009B2DB0
  bb_009B2D5C -->|fallthrough| bb_009B2D9D
  bb_009B2DAF -->|flow| bb_009B2DB0
  bb_009B2DB0 -->|branch| bb_009B2D9D
```
