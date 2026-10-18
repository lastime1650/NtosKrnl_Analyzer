# SysCtxRegOpenKey

- RVA: `0x008ED810`–`0x008ED85C` (길이 `76` bytes)
- VA: `0x00000001408ED810`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086DE4`
- 디코드: `22`개 명령, `76/76` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008ED845` → [_RegRtlOpenKeyTransacted](_RegRtlOpenKeyTransacted_function_008EF810.md) (function, `0x008EF810`)

### Direct callers
- [SysCtxRegOpenCurrentUserKey](../8F/SysCtxRegOpenCurrentUserKey_function_008F455C.md) at `0x008F479F`
- [PiDrvDbLoadNodeWorkerCallback](../A9/PiDrvDbLoadNodeWorkerCallback_function_00A91D40.md) at `0x00A91E29`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008ED810  40 53                           push rbx
008ED812  48 83 EC 30                     sub rsp, 0x30
008ED816  45 8B D1                        mov r10d, r9d
008ED819  4D 8B D8                        mov r11, r8
008ED81C  48 8B DA                        mov rbx, rdx
008ED81F  48 85 C9                        test rcx, rcx
008ED822  74 2D                           je 0x1408ed851
008ED824  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
008ED828  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008ED82D  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008ED832  45 8B C2                        mov r8d, r10d
008ED835  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
008ED83A  49 8B D3                        mov rdx, r11
008ED83D  48 8B CB                        mov rcx, rbx
008ED840  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008ED845  E8 C6 1F 00 00                  call 0x1408ef810
008ED84A  48 83 C4 30                     add rsp, 0x30
008ED84E  5B                              pop rbx
008ED84F  C3                              ret
008ED850  CC                              int3
008ED851  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
008ED85A  EB D1                           jmp 0x1408ed82d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SysCtxRegOpenKey(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p28;

    v_rsp = (v_rsp) - (48);
    if (a1 == 0) goto loc_008ED851;
    v_stack_m10 = *(unsigned __int64 *)(a1 + 8);
loc_008ED82D:
    v_stack_m18 = a6;
    result = _RegRtlOpenKeyTransacted(a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(a5));
    v_rsp = (v_rsp) + (48);
    return result;
loc_008ED851:
    v_stack_p28 = 0;
    goto loc_008ED82D;
}
```

## 5. (Beta) C Style

```c
int64_t SysCtxRegOpenKey(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p28;

    local_rsp = (local_rsp) - (48);
    if (Arg1 == 0) goto loc_008ED851;
    v_stack_m10 = *(uint64_t *)(Arg1 + 0x8);
loc_008ED82D:
    v_stack_m18 = Arg6;
    result = _RegRtlOpenKeyTransacted(Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(Arg5));
    local_rsp = (local_rsp) + (48);
    return result;
loc_008ED851:
    v_stack_p28 = 0;
    goto loc_008ED82D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008ED810&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008ED810[BB_008ED810]
  bb_008ED824[BB_008ED824]
  bb_008ED82D[BB_008ED82D]
  bb_008ED850[BB_008ED850]
  bb_008ED851[BB_008ED851]
  bb_008ED810 -->|branch| bb_008ED851
  bb_008ED810 -->|fallthrough| bb_008ED824
  bb_008ED824 -->|flow| bb_008ED82D
  bb_008ED850 -->|flow| bb_008ED851
  bb_008ED851 -->|branch| bb_008ED82D
```
