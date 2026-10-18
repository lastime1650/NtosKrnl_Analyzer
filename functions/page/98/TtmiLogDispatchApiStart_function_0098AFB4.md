# TtmiLogDispatchApiStart

- RVA: `0x0098AFB4`–`0x0098B07C` (길이 `200` bytes)
- VA: `0x000000014098AFB4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000986F8`
- 디코드: `42`개 명령, `200/200` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0098AFEA` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0098B003` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0098B05D` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0098B06D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmDispatchApi](TtmDispatchApi_function_0098AD08.md) at `0x0098AD2F`

### Static image references
- `0x0098AFBD` → RVA `0x00E0A740` (`.data`; read)
- `0x0098AFCF` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0098B052` → RVA `0x0005209C` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0098AFEA` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0098B003` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0098B05D` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0098B06D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098AFB4  40 53                           push rbx
0098AFB6  48 81 EC 90 00 00 00            sub rsp, 0x90
0098AFBD  48 8B 05 7C F7 47 00            mov rax, qword ptr [rip + 0x47f77c]
0098AFC4  48 33 C4                        xor rax, rsp
0098AFC7  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0098AFCF  83 3D F2 D8 64 00 05            cmp dword ptr [rip + 0x64d8f2], 5
0098AFD6  8B D9                           mov ebx, ecx
0098AFD8  0F 86 84 00 00 00               jbe 0x14098b062
0098AFDE  BA 01 00 00 00                  mov edx, 1
0098AFE3  48 8D 0D DE D8 64 00            lea rcx, [rip + 0x64d8de]
0098AFEA  E8 B1 3A AA FF                  call 0x14042eaa0
0098AFEF  84 C0                           test al, al
0098AFF1  74 6F                           je 0x14098b062
0098AFF3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0098AFFC  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0098B003  E8 E8 48 8A FF                  call 0x14022f8f0
0098B008  83 64 24 6C 00                  and dword ptr [rsp + 0x6c], 0
0098B00D  48 8D 0D B4 D8 64 00            lea rcx, [rip + 0x64d8b4]
0098B014  83 64 24 7C 00                  and dword ptr [rsp + 0x7c], 0
0098B019  BA 04 00 00 00                  mov edx, 4
0098B01E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0098B022  45 33 C9                        xor r9d, r9d
0098B025  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0098B02A  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
0098B02E  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0098B033  45 33 C0                        xor r8d, r8d
0098B036  48 8D 44 24 34                  lea rax, [rsp + 0x34]
0098B03B  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
0098B03F  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0098B044  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0098B049  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0098B04E  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
0098B052  48 8D 15 43 70 6C FF            lea rdx, [rip - 0x938fbd]
0098B059  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
0098B05D  E8 7E B0 A9 FF                  call 0x1404260e0
0098B062  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0098B06A  48 33 CC                        xor rcx, rsp
0098B06D  E8 CE 15 D2 FF                  call 0x1406ac640
0098B072  48 81 C4 90 00 00 00            add rsp, 0x90
0098B079  5B                              pop rbx
0098B07A  C3                              ret
0098B07B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDispatchApiStart(int a1, __int64 a2, int a3, int a4)
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
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;

    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 4716412)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 6609138)) <= 5) goto loc_0098B062;
    result = tlgKeywordOn(v_rip + 6609118, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 6609076;
        a2 = 4;
        v_stack_m68 = (unsigned int)(result);
        a4 = 0;
        result = v_stack_m68;
        v_stack_m30 = (unsigned int)(a2);
        v_stack_m38 = result;
        a3 = 0;
        result = v_stack_m64;
        v_stack_m20 = (unsigned int)(a2);
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = (unsigned int)(a2);
        a2 = v_rip - 9670589;
        v_stack_m64 = (unsigned int)((unsigned int)(a1));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDispatchApiStart(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;

    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x47F77C)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x64D8F2)) <= 5) goto loc_0098B062;
    result = tlgKeywordOn(v_rip + 6609118, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 6609076;
        Arg2 = 4;
        v_stack_m68 = (uint32_t)(result);
        Arg4 = 0;
        result = v_stack_m68;
        v_stack_m30 = (uint32_t)(Arg2);
        v_stack_m38 = result;
        Arg3 = 0;
        result = v_stack_m64;
        v_stack_m20 = (uint32_t)(Arg2);
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = (uint32_t)(Arg2);
        Arg2 = v_rip - 9670589;
        v_stack_m64 = (uint32_t)((uint32_t)(Arg1));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098AFB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0098AFB4[BB_0098AFB4]
  bb_0098AFDE[BB_0098AFDE]
  bb_0098AFF3[BB_0098AFF3]
  bb_0098B062[BB_0098B062]
  bb_0098B07B[BB_0098B07B]
  bb_0098AFB4 -->|branch| bb_0098B062
  bb_0098AFB4 -->|fallthrough| bb_0098AFDE
  bb_0098AFDE -->|branch| bb_0098B062
  bb_0098AFDE -->|fallthrough| bb_0098AFF3
  bb_0098AFF3 -->|flow| bb_0098B062
```
