# CmpTraceHiveMountStart

- RVA: `0x009B80C8`–`0x009B812F` (길이 `103` bytes)
- VA: `0x00000001409B80C8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009E910`
- 디코드: `24`개 명령, `103/103` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009B80F4` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009B8105` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009B8128` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [HvHiveStartFileBacked](HvHiveStartFileBacked_function_009B7E20.md) at `0x009B7F0C`

### Static image references
- `0x009B80CC` → RVA `0x00E0A740` (`.data`; read)
- `0x009B80DB` → RVA `0x00013C90` (`.rdata`; read)
- `0x009B80E2` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009B80F4` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009B8105` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009B8128` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009B80C8  48 83 EC 58                     sub rsp, 0x58
009B80CC  48 8B 05 6D 26 45 00            mov rax, qword ptr [rip + 0x45266d]
009B80D3  48 33 C4                        xor rax, rsp
009B80D6  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009B80DB  0F 10 05 AE BB 65 FF            movups xmm0, xmmword ptr [rip - 0x9a4452]
009B80E2  48 8B 0D 2F FF 61 00            mov rcx, qword ptr [rip + 0x61ff2f]
009B80E9  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
009B80EE  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
009B80F4  E8 57 A3 9D FF                  call 0x140392450
009B80F9  84 C0                           test al, al
009B80FB  75 13                           jne 0x1409b8110
009B80FD  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009B8102  48 33 CC                        xor rcx, rsp
009B8105  E8 36 45 CF FF                  call 0x1406ac640
009B810A  48 83 C4 58                     add rsp, 0x58
009B810E  C3                              ret
009B810F  CC                              int3
009B8110  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
009B8116  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
009B811B  48 8B 0D F6 FE 61 00            mov rcx, qword ptr [rip + 0x61fef6]
009B8122  45 33 C9                        xor r9d, r9d
009B8125  45 33 C0                        xor r8d, r8d
009B8128  E8 F3 45 A6 FF                  call 0x14041c720
009B812D  EB CE                           jmp 0x1409b80fd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveMountStart(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 4531821)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6422319), v_stack_m28, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009B8110;
loc_009B80FD:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m28, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
loc_009B8110:
    a4 = 0;
    a3 = 0;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 6422262), v_stack_p30, a3, a4);
    goto loc_009B80FD;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveMountStart(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x45266D)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x61FF2F), v_stack_m28, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_009B8110;
loc_009B80FD:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m28, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
loc_009B8110:
    Arg4 = 0;
    Arg3 = 0;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x61FEF6), v_stack_p30, Arg3, Arg4);
    goto loc_009B80FD;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B80C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009B80C8[BB_009B80C8]
  bb_009B80FD[BB_009B80FD]
  bb_009B810F[BB_009B810F]
  bb_009B8110[BB_009B8110]
  bb_009B80C8 -->|branch| bb_009B8110
  bb_009B80C8 -->|fallthrough| bb_009B80FD
  bb_009B810F -->|flow| bb_009B8110
  bb_009B8110 -->|branch| bb_009B80FD
```
