# PopEnsureCoalescingWorkerWillRun

- RVA: `0x004C266C`–`0x004C269B` (길이 `47` bytes)
- VA: `0x00000001404C266C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00094EEC`
- 디코드: `13`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x004C2694` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [PopCoalescingNotify](../../page/75/PopCoalescingNotify_function_0075C0E0.md) at `0x0075C105`
- [PopCheckResiliencyScenarios](../../page/A3/PopCheckResiliencyScenarios_function_00A31718.md) at `0x00A317D7`
- [PopEnforceResiliencyScenarios](../../page/AC/PopEnforceResiliencyScenarios_function_00AC3D90.md) at `0x00AC3E08`

### Static image references
- `0x004C2670` → RVA `0x00F0E068` (`.data`; read)
- `0x004C2682` → RVA `0x00F0E040` (`.data`; read)
- `0x004C268E` → RVA `0x00F0E068` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C266C  48 83 EC 28                     sub rsp, 0x28
004C2670  8A 05 F2 B9 A4 00               mov al, byte ptr [rip + 0xa4b9f2]
004C2676  A8 08                           test al, 8
004C2678  74 06                           je 0x1404c2680
004C267A  48 83 C4 28                     add rsp, 0x28
004C267E  C3                              ret
004C267F  CC                              int3
004C2680  0C 08                           or al, 8
004C2682  48 8D 0D B7 B9 A4 00            lea rcx, [rip + 0xa4b9b7]
004C2689  BA 01 00 00 00                  mov edx, 1
004C268E  88 05 D4 B9 A4 00               mov byte ptr [rip + 0xa4b9d4], al
004C2694  E8 87 6E E3 FF                  call 0x1402f9520
004C2699  EB DF                           jmp 0x1404c267a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEnsureCoalescingWorkerWillRun(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rip + 10795506))) & (8)) == 0) goto loc_004C2680;
loc_004C267A:
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int8 *)(v_rip + 10795506);
loc_004C2680:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 10795506)) | (8));
    *(unsigned __int8 *)(v_rip + 10795476) = (unsigned __int8)(result);
    result = ExQueueWorkItem(v_rip + 10795447, 1, a3, a4);
    goto loc_004C267A;
}
```

## 5. (Beta) C Style

```c
void PopEnsureCoalescingWorkerWillRun(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)(*(uint8_t *)(v_rip + 0xA4B9F2))) & (8)) == 0) goto loc_004C2680;
loc_004C267A:
    local_rsp = (local_rsp) + (40);
    return *(uint8_t *)(v_rip + 0xA4B9F2);
loc_004C2680:
    result = (uint8_t)((*(uint8_t *)(v_rip + 0xA4B9F2)) | (8));
    *(uint8_t *)(v_rip + 0xA4B9D4) = (uint8_t)(result);
    result = ExQueueWorkItem(v_rip + 10795447, 1, a3, a4);
    goto loc_004C267A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C266C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C266C[BB_004C266C]
  bb_004C267A[BB_004C267A]
  bb_004C267F[BB_004C267F]
  bb_004C2680[BB_004C2680]
  bb_004C266C -->|branch| bb_004C2680
  bb_004C266C -->|fallthrough| bb_004C267A
  bb_004C267F -->|flow| bb_004C2680
  bb_004C2680 -->|branch| bb_004C267A
```
