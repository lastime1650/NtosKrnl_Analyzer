# InbvBitBlt

- RVA: `0x0059015C`–`0x00590182` (길이 `38` bytes)
- VA: `0x000000014059015C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00590177` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [DisplayBootBitmap](../53/DisplayBootBitmap_function_0053B87C.md) at `0x0053B934`
- [DisplayBootBitmap](../53/DisplayBootBitmap_function_0053B87C.md) at `0x0053B948`
- [DisplayBootBitmap](../53/DisplayBootBitmap_function_0053B87C.md) at `0x0053B99D`
- [DisplayBootBitmap](../53/DisplayBootBitmap_function_0053B87C.md) at `0x0053B9AD`

### Static image references
- `0x00590160` → RVA `0x00E65E58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0059015C  48 83 EC 28                     sub rsp, 0x28
00590160  48 8B 05 F1 5C 8D 00            mov rax, qword ptr [rip + 0x8d5cf1]
00590167  48 85 C0                        test rax, rax
0059016A  74 10                           je 0x14059017c
0059016C  48 8B 40 60                     mov rax, qword ptr [rax + 0x60]
00590170  48 85 C0                        test rax, rax
00590173  74 07                           je 0x14059017c
00590175  33 D2                           xor edx, edx
00590177  E8 54 A9 12 00                  call 0x1406baad0
0059017C  48 83 C4 28                     add rsp, 0x28
00590180  C3                              ret
00590181  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall InbvBitBlt(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 9264369) == 0) goto loc_0059017C;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9264369) + 96);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9264369) + 96) != 0) {
        a2 = 0;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t InbvBitBlt(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x8D5CF1) == 0) goto loc_0059017C;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D5CF1) + 0x60);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D5CF1) + 0x60) != 0) {
        Arg2 = 0;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0059015C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0059015C[BB_0059015C]
  bb_0059016C[BB_0059016C]
  bb_00590175[BB_00590175]
  bb_0059017C[BB_0059017C]
  bb_00590181[BB_00590181]
  bb_0059015C -->|branch| bb_0059017C
  bb_0059015C -->|fallthrough| bb_0059016C
  bb_0059016C -->|branch| bb_0059017C
  bb_0059016C -->|fallthrough| bb_00590175
  bb_00590175 -->|flow| bb_0059017C
```
