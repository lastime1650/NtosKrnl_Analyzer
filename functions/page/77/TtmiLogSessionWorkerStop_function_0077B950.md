# TtmiLogSessionWorkerStop

- RVA: `0x0077B950`–`0x0077BA02` (길이 `178` bytes)
- VA: `0x000000014077B950`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9BCC`
- 디코드: `38`개 명령, `178/178` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077B984` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077B9E4` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077B9F4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpSessionWorker](TtmpSessionWorker_function_00777F60.md) at `0x007780DF`

### Static image references
- `0x0077B957` → RVA `0x00E0A740` (`.data`; read)
- `0x0077B969` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077B9DD` → RVA `0x00051DFE` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077B984` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077B9E4` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077B9F4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077B950  48 81 EC 98 00 00 00            sub rsp, 0x98
0077B957  48 8B 05 E2 ED 68 00            mov rax, qword ptr [rip + 0x68ede2]
0077B95E  48 33 C4                        xor rax, rsp
0077B961  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0077B969  83 3D 58 CF 85 00 05            cmp dword ptr [rip + 0x85cf58], 5
0077B970  44 8B C2                        mov r8d, edx
0077B973  44 8B C9                        mov r9d, ecx
0077B976  76 71                           jbe 0x14077b9e9
0077B978  BA 01 00 00 00                  mov edx, 1
0077B97D  48 8D 0D 44 CF 85 00            lea rcx, [rip + 0x85cf44]
0077B984  E8 17 31 CB FF                  call 0x14042eaa0
0077B989  84 C0                           test al, al
0077B98B  74 5C                           je 0x14077b9e9
0077B98D  83 64 24 6C 00                  and dword ptr [rsp + 0x6c], 0
0077B992  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0077B997  83 64 24 7C 00                  and dword ptr [rsp + 0x7c], 0
0077B99C  48 8D 0D 25 CF 85 00            lea rcx, [rip + 0x85cf25]
0077B9A3  BA 04 00 00 00                  mov edx, 4
0077B9A8  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0077B9AD  48 8D 44 24 34                  lea rax, [rsp + 0x34]
0077B9B2  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
0077B9B7  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0077B9BC  45 33 C9                        xor r9d, r9d
0077B9BF  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0077B9C4  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
0077B9C8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077B9CD  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
0077B9D1  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
0077B9D6  45 33 C0                        xor r8d, r8d
0077B9D9  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
0077B9DD  48 8D 15 1A 64 8D FF            lea rdx, [rip - 0x729be6]
0077B9E4  E8 F7 A6 CA FF                  call 0x1404260e0
0077B9E9  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0077B9F1  48 33 CC                        xor rcx, rsp
0077B9F4  E8 47 0C F3 FF                  call 0x1406ac640
0077B9F9  48 81 C4 98 00 00 00            add rsp, 0x98
0077BA00  C3                              ret
0077BA01  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogSessionWorkerStop(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;

    v_rsp = (v_rsp) - (152);
    result = (*(unsigned __int64 *)(v_rip + 6876642)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8769368)) <= 5) goto loc_0077B9E9;
    result = tlgKeywordOn(v_rip + 8769348, 1, (unsigned int)(a2), (unsigned int)(a1));
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m68;
        a1 = v_rip + 8769317;
        a2 = 4;
        v_stack_m38 = result;
        result = v_stack_m64;
        v_stack_m68 = (unsigned int)((unsigned int)(a1));
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m58;
        v_stack_m30 = a2;
        v_stack_m70 = result;
        v_stack_m78 = a2;
        v_stack_m64 = (unsigned int)((unsigned int)(a2));
        a3 = 0;
        v_stack_m20 = a2;
        a2 = v_rip - 7511014;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (152);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogSessionWorkerStop(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m58;
    uint64_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;

    local_rsp = (local_rsp) - (152);
    result = (*(uint64_t *)(v_rip + 0x68EDE2)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85CF58)) <= 5) goto loc_0077B9E9;
    result = tlgKeywordOn(v_rip + 8769348, 1, (uint32_t)(Arg2), (uint32_t)(Arg1));
    if ((uint8_t)(result) != 0) {
        result = v_stack_m68;
        Arg1 = v_rip + 8769317;
        Arg2 = 4;
        v_stack_m38 = result;
        result = v_stack_m64;
        v_stack_m68 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m58;
        v_stack_m30 = Arg2;
        v_stack_m70 = result;
        v_stack_m78 = Arg2;
        v_stack_m64 = (uint32_t)((uint32_t)(Arg2));
        a3 = 0;
        v_stack_m20 = Arg2;
        Arg2 = v_rip - 7511014;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (152);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077B950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077B950[BB_0077B950]
  bb_0077B978[BB_0077B978]
  bb_0077B98D[BB_0077B98D]
  bb_0077B9E9[BB_0077B9E9]
  bb_0077BA01[BB_0077BA01]
  bb_0077B950 -->|branch| bb_0077B9E9
  bb_0077B950 -->|fallthrough| bb_0077B978
  bb_0077B978 -->|branch| bb_0077B9E9
  bb_0077B978 -->|fallthrough| bb_0077B98D
  bb_0077B98D -->|flow| bb_0077B9E9
```
