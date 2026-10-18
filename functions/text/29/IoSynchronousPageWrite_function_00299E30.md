# IoSynchronousPageWrite

- RVA: `0x00299E30`–`0x00299E54` (길이 `36` bytes)
- VA: `0x0000000140299E30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `9`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00299E49` → [IoSynchronousPageWriteEx](IoSynchronousPageWriteEx_function_0029A860.md) (function, `0x0029A860`)

### Direct callers
- [SmKmStoreFileWriteHeader](../../page/7A/SmKmStoreFileWriteHeader_function_007A9DB4.md) at `0x007A9F1B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00299E30  48 83 EC 48                     sub rsp, 0x48
00299E34  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00299E39  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00299E3E  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00299E44  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00299E49  E8 12 0A 00 00                  call 0x14029a860
00299E4E  48 83 C4 48                     add rsp, 0x48
00299E52  C3                              ret
00299E53  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoSynchronousPageWrite(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int8 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = a5;
    v_stack_m28 = 0;
    result = IoSynchronousPageWriteEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoSynchronousPageWrite(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint8_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = Arg5;
    v_stack_m28 = 0;
    result = IoSynchronousPageWriteEx(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00299E30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00299E30[BB_00299E30]
  bb_00299E53[BB_00299E53]
```
