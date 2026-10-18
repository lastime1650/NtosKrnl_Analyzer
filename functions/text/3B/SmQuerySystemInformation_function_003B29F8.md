# SmQuerySystemInformation

- RVA: `0x003B29F8`–`0x003B2A7C` (길이 `132` bytes)
- VA: `0x00000001403B29F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C434`
- 디코드: `35`개 명령, `132/132` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003B2A33` → [KeStackAttachProcess](../21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x003B2A46` → [ZwQuerySystemInformation](../6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)
- `0x003B2A54` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x003B2A63` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmHighMemPriorityWatchdogWorker](../34/SMKM_STORE_MGR_SM_TRAITS_SmHighMemPriorityWatchdogWorker_function_0034C080.md) at `0x0034C0CB`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmStart](ST_STORE_SM_TRAITS_StDmStart_function_003B25C8.md) at `0x003B2860`

### Static image references
- `0x003B29FE` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003B29F8  40 53                           push rbx
003B29FA  48 83 EC 60                     sub rsp, 0x60
003B29FE  48 8B 05 3B 7D A5 00            mov rax, qword ptr [rip + 0xa57d3b]
003B2A05  48 33 C4                        xor rax, rsp
003B2A08  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003B2A0D  0F 57 C0                        xorps xmm0, xmm0
003B2A10  49 8B D8                        mov rbx, r8
003B2A13  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
003B2A18  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
003B2A1D  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
003B2A22  F6 C1 01                        test cl, 1
003B2A25  75 48                           jne 0x1403b2a6f
003B2A27  48 8B 89 78 08 00 00            mov rcx, qword ptr [rcx + 0x878]
003B2A2E  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
003B2A33  E8 C8 3D E6 FF                  call 0x140216800
003B2A38  45 33 C9                        xor r9d, r9d
003B2A3B  48 8B D3                        mov rdx, rbx
003B2A3E  45 8D 41 38                     lea r8d, [r9 + 0x38]
003B2A42  41 8D 48 7E                     lea ecx, [r8 + 0x7e]
003B2A46  E8 45 AD 2F 00                  call 0x1406ad790
003B2A4B  33 D2                           xor edx, edx
003B2A4D  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
003B2A52  8B D8                           mov ebx, eax
003B2A54  E8 D7 52 E6 FF                  call 0x140217d30
003B2A59  8B C3                           mov eax, ebx
003B2A5B  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003B2A60  48 33 CC                        xor rcx, rsp
003B2A63  E8 D8 9B 2F 00                  call 0x1406ac640
003B2A68  48 83 C4 60                     add rsp, 0x60
003B2A6C  5B                              pop rbx
003B2A6D  C3                              ret
003B2A6E  CC                              int3
003B2A6F  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
003B2A73  48 8B 89 90 1D 00 00            mov rcx, qword ptr [rcx + 0x1d90]
003B2A7A  EB AB                           jmp 0x1403b2a27
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmQuerySystemInformation(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 10845499)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_003B2A6F;
loc_003B2A27:
    result = KeStackAttachProcess(*(unsigned __int64 *)(a1 + 2168), v_stack_m48, a3, a4);
    a4 = 0;
    result = ZwQuerySystemInformation(a4 + 56 + 126, a3, a4 + 56, a4);
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m48, a2, a4 + 56, a4);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a4 + 56, a4);
    v_rsp = (v_rsp) + (96);
    return result;
loc_003B2A6F:
    a1 = (a1) & (-2);
    goto loc_003B2A27;
}
```

## 5. (Beta) C Style

```c
int64_t SmQuerySystemInformation(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0xA57D3B)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_003B2A6F;
loc_003B2A27:
    result = KeStackAttachProcess(*(uint64_t *)(Arg1 + 0x878), v_stack_m48, Arg3, Arg4);
    Arg4 = 0;
    result = ZwQuerySystemInformation(Arg4 + 56 + 126, Arg3, Arg4 + 56, Arg4);
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m48, Arg2, Arg4 + 56, Arg4);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg4 + 56, Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
loc_003B2A6F:
    Arg1 = (Arg1) & (-2);
    goto loc_003B2A27;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B29F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003B29F8[BB_003B29F8]
  bb_003B2A27[BB_003B2A27]
  bb_003B2A6E[BB_003B2A6E]
  bb_003B2A6F[BB_003B2A6F]
  bb_003B29F8 -->|branch| bb_003B2A6F
  bb_003B29F8 -->|fallthrough| bb_003B2A27
  bb_003B2A6E -->|flow| bb_003B2A6F
  bb_003B2A6F -->|branch| bb_003B2A27
```
