# BvgaAcquireDisplayOwnership

- RVA: `0x00591360`–`0x00591393` (길이 `51` bytes)
- VA: `0x0000000140591360`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00591381` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [BvgaNotifyDisplayOwnershipChange](BvgaNotifyDisplayOwnershipChange_function_005915C0.md) at `0x005915DC`

### Static image references
- `0x00591364` → RVA `0x00E65EC0` (`.data`; read)
- `0x00591370` → RVA `0x00E65ED0` (`.data`; read)
- `0x00591386` → RVA `0x00E65ED0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00591360  48 83 EC 28                     sub rsp, 0x28
00591364  48 8B 05 55 4B 8D 00            mov rax, qword ptr [rip + 0x8d4b55]
0059136B  48 85 C0                        test rax, rax
0059136E  74 16                           je 0x140591386
00591370  83 3D 59 4B 8D 00 02            cmp dword ptr [rip + 0x8d4b59], 2
00591377  75 0D                           jne 0x140591386
00591379  BA 32 00 00 00                  mov edx, 0x32
0059137E  8D 4A 1E                        lea ecx, [rdx + 0x1e]
00591381  E8 4A 97 12 00                  call 0x1406baad0
00591386  83 25 43 4B 8D 00 00            and dword ptr [rip + 0x8d4b43], 0
0059138D  48 83 C4 28                     add rsp, 0x28
00591391  C3                              ret
00591392  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BvgaAcquireDisplayOwnership(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 9259861) == 0) goto loc_00591386;
    result = *(unsigned __int64 *)(v_rip + 9259861);
    if ((*(unsigned int *)(v_rip + 9259865)) == 2) {
        a2 = 50;
        a1 = a2 + 30;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void BvgaAcquireDisplayOwnership(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x8D4B55) == 0) goto loc_00591386;
    result = *(uint64_t *)(v_rip + 0x8D4B55);
    if ((*(uint32_t *)(v_rip + 0x8D4B59)) == 2) {
        a2 = 50;
        a1 = a2 + 30;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00591360&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00591360[BB_00591360]
  bb_00591370[BB_00591370]
  bb_00591379[BB_00591379]
  bb_00591386[BB_00591386]
  bb_00591392[BB_00591392]
  bb_00591360 -->|branch| bb_00591386
  bb_00591360 -->|fallthrough| bb_00591370
  bb_00591370 -->|branch| bb_00591386
  bb_00591370 -->|fallthrough| bb_00591379
  bb_00591379 -->|flow| bb_00591386
```
