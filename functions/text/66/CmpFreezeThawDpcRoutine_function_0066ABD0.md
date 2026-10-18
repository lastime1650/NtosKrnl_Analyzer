# CmpFreezeThawDpcRoutine

- RVA: `0x0066ABD0`–`0x0066ABF7` (길이 `39` bytes)
- VA: `0x000000014066ABD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0066ABEC` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0066ABDB` → RVA `0x00EEFBFC` (`.data`; read)
- `0x0066ABE5` → RVA `0x00EF71A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066ABD0  48 83 EC 28                     sub rsp, 0x28
0066ABD4  BA 01 00 00 00                  mov edx, 1
0066ABD9  33 C0                           xor eax, eax
0066ABDB  F0 0F B1 15 19 50 88 00         lock cmpxchg dword ptr [rip + 0x885019], edx
0066ABE3  75 0C                           jne 0x14066abf1
0066ABE5  48 8D 0D B4 C5 88 00            lea rcx, [rip + 0x88c5b4]
0066ABEC  E8 2F E9 C8 FF                  call 0x1402f9520
0066ABF1  48 83 C4 28                     add rsp, 0x28
0066ABF5  C3                              ret
0066ABF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFreezeThawDpcRoutine(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (!(condition_is_not_equal)) {
        a1 = v_rip + 8963508;
        result = ExQueueWorkItem(a1, 1, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void CmpFreezeThawDpcRoutine(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (!(condition_is_not_equal)) {
        a1 = v_rip + 8963508;
        result = ExQueueWorkItem(a1, 1, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066ABD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066ABD0[BB_0066ABD0]
  bb_0066ABE5[BB_0066ABE5]
  bb_0066ABF1[BB_0066ABF1]
  bb_0066ABF6[BB_0066ABF6]
  bb_0066ABD0 -->|branch| bb_0066ABF1
  bb_0066ABD0 -->|fallthrough| bb_0066ABE5
  bb_0066ABE5 -->|flow| bb_0066ABF1
```
