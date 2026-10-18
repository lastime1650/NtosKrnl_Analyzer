# MinAsn1ParseECCSignature

- RVA: `0x006A6464`–`0x006A6473` (길이 `15` bytes)
- VA: `0x00000001406A6464`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006A6468` → [MinAsn1ParseRSAPublicKey](../../page/83/MinAsn1ParseRSAPublicKey_function_00838EDC.md) (function, `0x00838EDC`)

### Direct callers
- [MinCryptVerifySignedHash2](../../page/83/MinCryptVerifySignedHash2_function_008362A0.md) at `0x008363B1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006A6468` → [MinAsn1ParseRSAPublicKey](../../page/83/MinAsn1ParseRSAPublicKey_function_00838EDC.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A6464  48 83 EC 28                     sub rsp, 0x28
006A6468  E8 6F 2A 19 00                  call 0x140838edc
006A646D  48 83 C4 28                     add rsp, 0x28
006A6471  C3                              ret
006A6472  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MinAsn1ParseECCSignature(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MinAsn1ParseRSAPublicKey(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MinAsn1ParseECCSignature(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MinAsn1ParseRSAPublicKey(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A6464&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A6464[BB_006A6464]
  bb_006A6472[BB_006A6472]
```
