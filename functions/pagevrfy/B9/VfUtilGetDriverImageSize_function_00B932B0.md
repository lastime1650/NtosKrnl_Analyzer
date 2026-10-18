# VfUtilGetDriverImageSize

- RVA: `0x00B932B0`–`0x00B932C8` (길이 `24` bytes)
- VA: `0x0000000140B932B0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B932B4` → [VfTargetDriversGetNode](../../text/3E/VfTargetDriversGetNode_function_003EE174.md) (function, `0x003EE174`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B932B4` → [VfTargetDriversGetNode](../../text/3E/VfTargetDriversGetNode_function_003EE174.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B932B0  48 83 EC 28                     sub rsp, 0x28
00B932B4  E8 BB AE 85 FF                  call 0x1403ee174
00B932B9  48 85 C0                        test rax, rax
00B932BC  74 04                           je 0x140b932c2
00B932BE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B932C2  48 83 C4 28                     add rsp, 0x28
00B932C6  C3                              ret
00B932C7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfUtilGetDriverImageSize(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = VfTargetDriversGetNode(a1, a2, a3, a4);
    if (result != 0) {
        result = *(unsigned __int64 *)(result + 8);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void VfUtilGetDriverImageSize(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = VfTargetDriversGetNode(a1, a2, a3, a4);
    if (result != 0) {
        result = *(uint64_t *)(result + 0x8);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B932B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B932B0[BB_00B932B0]
  bb_00B932BE[BB_00B932BE]
  bb_00B932C2[BB_00B932C2]
  bb_00B932C7[BB_00B932C7]
  bb_00B932B0 -->|branch| bb_00B932C2
  bb_00B932B0 -->|fallthrough| bb_00B932BE
  bb_00B932BE -->|flow| bb_00B932C2
```
