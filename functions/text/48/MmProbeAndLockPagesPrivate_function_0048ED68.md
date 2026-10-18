# MmProbeAndLockPagesPrivate

- RVA: `0x0048ED68`–`0x0048ED7F` (길이 `23` bytes)
- VA: `0x000000014048ED68`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0048ED74` → [MiProbeAndLockPages](../23/MiProbeAndLockPages_function_0023B4F0.md) (function, `0x0023B4F0`)

### Direct callers
- [WbCreateHeapExecutedBlock](../../page/8D/WbCreateHeapExecutedBlock_function_008D4BE8.md) at `0x008D4D2E`
- [WbCreateHeapExecutedBlock](../../page/8D/WbCreateHeapExecutedBlock_function_008D4BE8.md) at `0x008D4E61`
- [WbCreateHeapExecutedBlock](../../page/8D/WbCreateHeapExecutedBlock_function_008D4BE8.md) at `0x008D4FEE`
- [WbMakeUserExecutablePagesKernelWritable](../../page/9A/WbMakeUserExecutablePagesKernelWritable_function_009A14F4.md) at `0x009A1541`
- [sub_00B1B9DE](../../page/B1/Unknown_function_00B1B9DE.md) at `0x00B1BA35`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048ED68  48 83 EC 28                     sub rsp, 0x28
0048ED6C  41 B8 03 00 00 00               mov r8d, 3
0048ED72  B2 01                           mov dl, 1
0048ED74  E8 77 C7 DA FF                  call 0x14023b4f0
0048ED79  48 83 C4 28                     add rsp, 0x28
0048ED7D  C3                              ret
0048ED7E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmProbeAndLockPagesPrivate(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiProbeAndLockPages(a1, 1, 3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MmProbeAndLockPagesPrivate(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiProbeAndLockPages(a1, 1, 3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048ED68&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048ED68[BB_0048ED68]
  bb_0048ED7E[BB_0048ED7E]
```
