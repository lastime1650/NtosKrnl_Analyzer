# SepDereferenceCachedHandlesEntry

- RVA: `0x00A19400`–`0x00A1941B` (길이 `27` bytes)
- VA: `0x0000000140A19400`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A19410` → [SepDereferenceCachedHandlesEntryInternal](SepDereferenceCachedHandlesEntryInternal_function_00A19424.md) (function, `0x00A19424`)

### Direct callers
- [SepSetTokenBnoIsolation](../../text/49/SepSetTokenBnoIsolation_function_0049002C.md) at `0x004900DB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A19400  48 83 EC 28                     sub rsp, 0x28
00A19404  4C 8B C2                        mov r8, rdx
00A19407  48 83 C1 60                     add rcx, 0x60
00A1940B  33 D2                           xor edx, edx
00A1940D  45 33 C9                        xor r9d, r9d
00A19410  E8 0F 00 00 00                  call 0x140a19424
00A19415  48 83 C4 28                     add rsp, 0x28
00A19419  C3                              ret
00A1941A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepDereferenceCachedHandlesEntry(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) + (96);
    a2 = 0;
    a4 = 0;
    result = SepDereferenceCachedHandlesEntryInternal(a1, a2, a2, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepDereferenceCachedHandlesEntry(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) + (96);
    Arg2 = 0;
    Arg4 = 0;
    result = SepDereferenceCachedHandlesEntryInternal(Arg1, Arg2, Arg2, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A19400&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A19400[BB_00A19400]
  bb_00A1941A[BB_00A1941A]
```
