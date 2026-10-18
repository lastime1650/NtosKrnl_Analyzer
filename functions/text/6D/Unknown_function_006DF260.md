# sub_006DF260

- RVA: `0x006DF260`–`0x006DF275` (길이 `21` bytes)
- VA: `0x00000001406DF260`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071F9C`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DF26A` → [ZwRaiseException](../6A/ZwRaiseException_function_006AFF70.md) (function, `0x006AFF70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DF270` → [RtlUnwindEx + 0x382](../2F/RtlUnwindEx_function_002F2830.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DF260  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
006DF264  45 33 C0                        xor r8d, r8d
006DF267  48 8B D6                        mov rdx, rsi
006DF26A  E8 01 0D FD FF                  call 0x1406aff70
006DF26F  90                              nop
006DF270  E9 3D 39 C1 FF                  jmp 0x1402f2bb2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DF260(__int64 a1, __int64 a2, int a3)
{
    __int64 result;

    a3 = 0;
    result = ZwRaiseException(*(unsigned __int64 *)(v_rbp + 80), v_rsi, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DF260(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;

    Arg3 = 0;
    result = ZwRaiseException(*(uint64_t *)(local_rbp + 0x50), local_rsi, Arg3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DF260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DF260[BB_006DF260]
```
