# HalpPmuArbiterPeriodicTimerCallback

- RVA: `0x00547540`–`0x00547567` (길이 `39` bytes)
- VA: `0x0000000140547540`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0054755C` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0054754B` → RVA `0x00FC2B98` (`.data`; read/write)
- `0x00547555` → RVA `0x00FC2B78` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00547540  48 83 EC 28                     sub rsp, 0x28
00547544  BA 01 00 00 00                  mov edx, 1
00547549  8B C2                           mov eax, edx
0054754B  87 05 47 B6 A7 00               xchg dword ptr [rip + 0xa7b647], eax
00547551  85 C0                           test eax, eax
00547553  75 0C                           jne 0x140547561
00547555  48 8D 0D 1C B6 A7 00            lea rcx, [rip + 0xa7b61c]
0054755C  E8 BF 1F DB FF                  call 0x1402f9520
00547561  48 83 C4 28                     add rsp, 0x28
00547565  C3                              ret
00547566  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpPmuArbiterPeriodicTimerCallback(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 1;
    if (1 == 0) {
        a1 = v_rip + 10991132;
        result = ExQueueWorkItem(a1, 1, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpPmuArbiterPeriodicTimerCallback(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 1;
    if (1 == 0) {
        a1 = v_rip + 10991132;
        result = ExQueueWorkItem(a1, 1, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00547540&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00547540[BB_00547540]
  bb_00547555[BB_00547555]
  bb_00547561[BB_00547561]
  bb_00547566[BB_00547566]
  bb_00547540 -->|branch| bb_00547561
  bb_00547540 -->|fallthrough| bb_00547555
  bb_00547555 -->|flow| bb_00547561
```
