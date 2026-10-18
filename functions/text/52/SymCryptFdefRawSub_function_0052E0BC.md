# SymCryptFdefRawSub

- RVA: `0x0052E0BC`–`0x0052E0CB` (길이 `15` bytes)
- VA: `0x000000014052E0BC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0052E0C0` → [SymCryptFdefRawSubAsm](../53/SymCryptFdefRawSubAsm_function_00536570.md) (function, `0x00536570`)

### Direct callers
- [SymCryptFdefModAddGeneric](../53/SymCryptFdefModAddGeneric_function_00534200.md) at `0x00534268`
- [SymCryptFdefModNegGeneric](../53/SymCryptFdefModNegGeneric_function_00534F70.md) at `0x00534FCE`
- [SymCryptFdefModSubGeneric](../53/SymCryptFdefModSubGeneric_function_00535450.md) at `0x0053549F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052E0BC  48 83 EC 28                     sub rsp, 0x28
0052E0C0  E8 AB 84 00 00                  call 0x140536570
0052E0C5  48 83 C4 28                     add rsp, 0x28
0052E0C9  C3                              ret
0052E0CA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefRawSub(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = SymCryptFdefRawSubAsm(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void SymCryptFdefRawSub(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = SymCryptFdefRawSubAsm(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052E0BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052E0BC[BB_0052E0BC]
  bb_0052E0CA[BB_0052E0CA]
```
