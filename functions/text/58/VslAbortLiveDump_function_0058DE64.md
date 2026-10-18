# VslAbortLiveDump

- RVA: `0x0058DE64`–`0x0058DEBA` (길이 `86` bytes)
- VA: `0x000000014058DE64`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AA6F8`
- 디코드: `19`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0058DE88` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0058DE9C` → [VslpEnterIumSecureMode](../23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x0058DEAC` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IopLiveDumpFreeDumpBuffers](../3F/IopLiveDumpFreeDumpBuffers_function_003F5FE8.md) at `0x003F601F`
- [HvlPrepareLivedumpDescriptor](HvlPrepareLivedumpDescriptor_function_0058B734.md) at `0x0058B802`
- [VslFinalizeLiveDumpInSk](VslFinalizeLiveDumpInSk_function_0058E16C.md) at `0x0058E22F`

### Static image references
- `0x0058DE6B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058DE64  48 81 EC A8 00 00 00            sub rsp, 0xa8
0058DE6B  48 8B 05 CE C8 87 00            mov rax, qword ptr [rip + 0x87c8ce]
0058DE72  48 33 C4                        xor rax, rsp
0058DE75  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0058DE7D  33 D2                           xor edx, edx
0058DE7F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0058DE84  44 8D 42 68                     lea r8d, [rdx + 0x68]
0058DE88  E8 B3 8D 13 00                  call 0x1406c6c40
0058DE8D  BA 3F 00 00 00                  mov edx, 0x3f
0058DE92  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
0058DE97  45 33 C0                        xor r8d, r8d
0058DE9A  B1 02                           mov cl, 2
0058DE9C  E8 AF 7F CA FF                  call 0x140235e50
0058DEA1  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0058DEA9  48 33 CC                        xor rcx, rsp
0058DEAC  E8 8F E7 11 00                  call 0x1406ac640
0058DEB1  48 81 C4 A8 00 00 00            add rsp, 0xa8
0058DEB8  C3                              ret
0058DEB9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslAbortLiveDump(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (168);
    result = (*(unsigned __int64 *)(v_rip + 8898766)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 63, a3, v_stack_m88);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 63, a3, v_stack_m88);
    v_rsp = (v_rsp) + (168);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslAbortLiveDump(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (168);
    result = (*(uint64_t *)(v_rip + 0x87C8CE)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 63, a3, v_stack_m88);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 63, a3, v_stack_m88);
    local_rsp = (local_rsp) + (168);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058DE64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058DE64[BB_0058DE64]
  bb_0058DEB9[BB_0058DEB9]
```
