# MinCryptVerifySignedHash

- RVA: `0x00836278`–`0x00836297` (길이 `31` bytes)
- VA: `0x0000000140836278`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `8`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0083628C` → [MinCryptVerifySignedHash2](MinCryptVerifySignedHash2_function_008362A0.md) (function, `0x008362A0`)

### Direct callers
- [MinCryptCheckCertsAndKeys](../../text/6A/MinCryptCheckCertsAndKeys_function_006A61F8.md) at `0x006A62CE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00836278  48 83 EC 38                     sub rsp, 0x38
0083627C  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00836281  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00836287  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0083628C  E8 0F 00 00 00                  call 0x1408362a0
00836291  48 83 C4 38                     add rsp, 0x38
00836295  C3                              ret
00836296  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MinCryptVerifySignedHash(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = a5;
    result = MinCryptVerifySignedHash2(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MinCryptVerifySignedHash(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = Arg5;
    result = MinCryptVerifySignedHash2(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00836278&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00836278[BB_00836278]
  bb_00836296[BB_00836296]
```
