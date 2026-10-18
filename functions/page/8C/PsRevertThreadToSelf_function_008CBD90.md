# PsRevertThreadToSelf

- RVA: `0x008CBD90`–`0x008CBDAF` (길이 `31` bytes)
- VA: `0x00000001408CBD90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008CBDA4` → [PsImpersonateClient](PsImpersonateClient_function_008CBE10.md) (function, `0x008CBE10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008CBD90  48 83 EC 38                     sub rsp, 0x38
008CBD94  45 33 C9                        xor r9d, r9d
008CBD97  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008CBD9F  45 33 C0                        xor r8d, r8d
008CBDA2  33 D2                           xor edx, edx
008CBDA4  E8 67 00 00 00                  call 0x1408cbe10
008CBDA9  48 83 C4 38                     add rsp, 0x38
008CBDAD  C3                              ret
008CBDAE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsRevertThreadToSelf(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a4 = 0;
    v_stack_m18 = 2;
    a3 = 0;
    a2 = 0;
    result = PsImpersonateClient(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsRevertThreadToSelf(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg4 = 0;
    v_stack_m18 = 2;
    Arg3 = 0;
    Arg2 = 0;
    result = PsImpersonateClient(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008CBD90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008CBD90[BB_008CBD90]
  bb_008CBDAE[BB_008CBDAE]
```
