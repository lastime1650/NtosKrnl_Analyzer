# sub_006F25AE

- RVA: `0x006F25AE`–`0x006F25C3` (길이 `21` bytes)
- VA: `0x00000001406F25AE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9D34`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F25B8` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F25BE` → [MiRevokeExecutePte + 0x96](../46/MiRevokeExecutePte_function_00460BA0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F25AE  45 33 C9                        xor r9d, r9d
006F25B1  48 8B D6                        mov rdx, rsi
006F25B4  45 8D 41 01                     lea r8d, [r9 + 1]
006F25B8  E8 B3 10 BA FF                  call 0x140293670
006F25BD  90                              nop
006F25BE  E9 73 E6 D6 FF                  jmp 0x140460c36
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F25AE(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;

    a4 = 0;
    result = MiInsertTbFlushEntry(a1, v_rsi, a4 + 1, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F25AE(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;

    Arg4 = 0;
    result = MiInsertTbFlushEntry(Arg1, local_rsi, Arg4 + 1, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F25AE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F25AE[BB_006F25AE]
```
