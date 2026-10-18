# SepDeleteLogonSessionClaims

- RVA: `0x00AAC8A4`–`0x00AAC8C9` (길이 `37` bytes)
- VA: `0x0000000140AAC8A4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EE6C`
- 디코드: `13`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AAC8BD` → [SepDeleteClaimAttributes](../A8/SepDeleteClaimAttributes_function_00A8F64C.md) (function, `0x00A8F64C`)

### Direct callers
- [SepDeleteLogonSessionTrack](SepDeleteLogonSessionTrack_function_00AA04E0.md) at `0x00AA064F`
- [SepDeReferenceLogonSession](../AF/SepDeReferenceLogonSession_function_00AF25EC.md) at `0x00AF27E7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAC8A4  40 53                           push rbx
00AAC8A6  48 83 EC 20                     sub rsp, 0x20
00AAC8AA  48 8B D9                        mov rbx, rcx
00AAC8AD  48 8B 49 78                     mov rcx, qword ptr [rcx + 0x78]
00AAC8B1  48 85 C9                        test rcx, rcx
00AAC8B4  75 07                           jne 0x140aac8bd
00AAC8B6  48 83 C4 20                     add rsp, 0x20
00AAC8BA  5B                              pop rbx
00AAC8BB  C3                              ret
00AAC8BC  CC                              int3
00AAC8BD  E8 8A 2D FE FF                  call 0x140a8f64c
00AAC8C2  48 83 63 78 00                  and qword ptr [rbx + 0x78], 0
00AAC8C7  EB ED                           jmp 0x140aac8b6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepDeleteLogonSessionClaims(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 120) != 0) goto loc_00AAC8BD;
loc_00AAC8B6:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00AAC8BD:
    result = SepDeleteClaimAttributes(*(unsigned __int64 *)(a1 + 120), a2, a3, a4);
    goto loc_00AAC8B6;
}
```

## 5. (Beta) C Style

```c
int64_t SepDeleteLogonSessionClaims(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x78) != 0) goto loc_00AAC8BD;
loc_00AAC8B6:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00AAC8BD:
    result = SepDeleteClaimAttributes(*(uint64_t *)(arg1 + 0x78), a2, a3, a4);
    goto loc_00AAC8B6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAC8A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AAC8A4[BB_00AAC8A4]
  bb_00AAC8B6[BB_00AAC8B6]
  bb_00AAC8BC[BB_00AAC8BC]
  bb_00AAC8BD[BB_00AAC8BD]
  bb_00AAC8A4 -->|branch| bb_00AAC8BD
  bb_00AAC8A4 -->|fallthrough| bb_00AAC8B6
  bb_00AAC8BC -->|flow| bb_00AAC8BD
  bb_00AAC8BD -->|branch| bb_00AAC8B6
```
