# MiUnlockMultipleZeroChunks

- RVA: `0x0031FB00`–`0x0031FB15` (길이 `21` bytes)
- VA: `0x000000014031FB00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000753C0`
- 디코드: `7`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiBackgroundZeroLocalPages](MiBackgroundZeroLocalPages_function_0031EF30.md) at `0x0031F3B1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0031FB0F` → [sub_0031FC3C](Unknown_function_0031FC3C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031FB00  40 53                           push rbx
0031FB02  57                              push rdi
0031FB03  48 83 EC 48                     sub rsp, 0x48
0031FB07  8B 79 08                        mov edi, dword ptr [rcx + 8]
0031FB0A  48 8B D9                        mov rbx, rcx
0031FB0D  85 FF                           test edi, edi
0031FB0F  0F 84 27 01 00 00               je 0x14031fc3c
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiUnlockMultipleZeroChunks(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
}
```

## 5. (Beta) C Style

```c
void MiUnlockMultipleZeroChunks(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031FB00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0031FB00[BB_0031FB00]
```
