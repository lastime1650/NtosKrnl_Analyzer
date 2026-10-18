# InbvAcquireLock

- RVA: `0x0059012C`–`0x00590153` (길이 `39` bytes)
- VA: `0x000000014059012C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00590148` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [DisplayBootBitmap](../53/DisplayBootBitmap_function_0053B87C.md) at `0x0053B898`
- [DisplayBootBitmap](../53/DisplayBootBitmap_function_0053B87C.md) at `0x0053BA09`
- [FinalizeBootLogo](FinalizeBootLogo_function_0059062C.md) at `0x00590630`
- [InbvRotateGuiBootDisplay](InbvRotateGuiBootDisplay_function_00590680.md) at `0x0059069B`

### Static image references
- `0x00590130` → RVA `0x00E65E58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0059012C  48 83 EC 28                     sub rsp, 0x28
00590130  48 8B 05 21 5D 8D 00            mov rax, qword ptr [rip + 0x8d5d21]
00590137  48 85 C0                        test rax, rax
0059013A  74 11                           je 0x14059014d
0059013C  48 8B 80 98 00 00 00            mov rax, qword ptr [rax + 0x98]
00590143  48 85 C0                        test rax, rax
00590146  74 05                           je 0x14059014d
00590148  E8 83 A9 12 00                  call 0x1406baad0
0059014D  48 83 C4 28                     add rsp, 0x28
00590151  C3                              ret
00590152  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall InbvAcquireLock(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 9264417) == 0) goto loc_0059014D;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9264417) + 152);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9264417) + 152) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void InbvAcquireLock(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x8D5D21) == 0) goto loc_0059014D;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D5D21) + 0x98);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D5D21) + 0x98) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0059012C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0059012C[BB_0059012C]
  bb_0059013C[BB_0059013C]
  bb_00590148[BB_00590148]
  bb_0059014D[BB_0059014D]
  bb_00590152[BB_00590152]
  bb_0059012C -->|branch| bb_0059014D
  bb_0059012C -->|fallthrough| bb_0059013C
  bb_0059013C -->|branch| bb_0059014D
  bb_0059013C -->|fallthrough| bb_00590148
  bb_00590148 -->|flow| bb_0059014D
```
