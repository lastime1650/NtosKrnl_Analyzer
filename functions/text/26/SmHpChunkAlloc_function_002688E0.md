# SmHpChunkAlloc

- RVA: `0x002688E0`–`0x002688FB` (길이 `27` bytes)
- VA: `0x00000001402688E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065190`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ST_STORE&lt;SM_TRAITS&gt;::StDmpSinglePageAdd](../20/ST_STORE_SM_TRAITS_StDmpSinglePageAdd_function_0020502C.md) at `0x00205283`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmpDummyPageRecordAllocate](../4B/ST_STORE_SM_TRAITS_StDmpDummyPageRecordAllocate_function_004BC160.md) at `0x004BC170`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002688E0  40 53                           push rbx
002688E2  55                              push rbp
002688E3  48 83 EC 48                     sub rsp, 0x48
002688E7  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
002688EC  33 ED                           xor ebp, ebp
002688EE  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002688F3  48 8B D9                        mov rbx, rcx
002688F6  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall SmHpChunkAlloc(__int64 a1)
{
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_rsp = (v_rsp) - (72);
    v_stack_p10 = v_rsi;
    v_rbp = 0;
    v_stack_p18 = v_rdi;
    v_stack_m18 = v_r12;
    return;
}
```

## 5. (Beta) C Style

```c
void SmHpChunkAlloc(int64_t Arg1)
{
    int64_t local_rbp;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    local_rsp = (local_rsp) - (72);
    v_stack_p10 = local_rsi;
    local_rbp = 0;
    v_stack_p18 = local_rdi;
    v_stack_m18 = local_r12;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002688E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002688E0[BB_002688E0]
```
