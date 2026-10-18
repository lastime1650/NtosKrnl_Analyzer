# MiInitializePfnEntriesRaw

- RVA: `0x00442A60`–`0x00442A7A` (길이 `26` bytes)
- VA: `0x0000000140442A60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A5338`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiCreateInitialLargeLeafPfns](MiCreateInitialLargeLeafPfns_function_004428E0.md) at `0x00442A04`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00442A78` → [sub_00442AC1](Unknown_function_00442AC1.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00442A60  40 53                           push rbx
00442A62  4F 8D 1C 40                     lea r11, [r8 + r8*2]
00442A66  48 8B DA                        mov rbx, rdx
00442A69  4C 8B D1                        mov r10, rcx
00442A6C  4C 8B CA                        mov r9, rdx
00442A6F  41 B8 00 00 00 00               mov r8d, 0
00442A75  4D 03 DB                        add r11, r11
00442A78  74 47                           je 0x140442ac1
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiInitializePfnEntriesRaw(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 v_r11;

    v_r11 = (a3 + a3 * 2) + (a3 + a3 * 2);
}
```

## 5. (Beta) C Style

```c
void MiInitializePfnEntriesRaw(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t local_r11;

    local_r11 = (Arg3 + Arg3 * 2) + (Arg3 + Arg3 * 2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0 + r8*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00442A60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00442A60[BB_00442A60]
```
