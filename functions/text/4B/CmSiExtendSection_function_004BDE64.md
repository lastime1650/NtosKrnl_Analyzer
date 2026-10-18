# CmSiExtendSection

- RVA: `0x004BDE64`–`0x004BDE7D` (길이 `25` bytes)
- VA: `0x00000001404BDE64`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085914`
- 디코드: `7`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BDE72` → [ZwExtendSection](../6A/ZwExtendSection_function_006AEE30.md) (function, `0x006AEE30`)

### Direct callers
- [HvpViewMapExtendStorage](../../page/9B/HvpViewMapExtendStorage_function_009B4EF8.md) at `0x009B4F86`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BDE64  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
004BDE69  48 83 EC 28                     sub rsp, 0x28
004BDE6D  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
004BDE72  E8 B9 0F 1F 00                  call 0x1406aee30
004BDE77  48 83 C4 28                     add rsp, 0x28
004BDE7B  C3                              ret
004BDE7C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSiExtendSection(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (40);
    result = ZwExtendSection(a1, v_stack_p10, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmSiExtendSection(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (40);
    result = ZwExtendSection(Arg1, v_stack_p10, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BDE64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BDE64[BB_004BDE64]
  bb_004BDE7C[BB_004BDE7C]
```
