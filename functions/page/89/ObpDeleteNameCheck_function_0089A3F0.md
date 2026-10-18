# ObpDeleteNameCheck

- RVA: `0x0089A3F0`–`0x0089A401` (길이 `17` bytes)
- VA: `0x000000014089A3F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E628`
- 디코드: `6`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ObpDereferenceNamedObject](../../text/3A/ObpDereferenceNamedObject_function_003A0310.md) at `0x003A034D`
- [ObpCreateHandle](../86/ObpCreateHandle_function_0086B950.md) at `0x0086D5B6`
- [ObpIncrementHandleCountEx](../86/ObpIncrementHandleCountEx_function_0086DA10.md) at `0x0086E0EB`
- [sub_0089A903](Unknown_function_0089A903.md) at `0x0089ACF6`
- [ObMakeTemporaryObject](../A7/ObMakeTemporaryObject_function_00A7F860.md) at `0x00A7F8F2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0089A3FF` → [sub_0089A436](Unknown_function_0089A436.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0089A3F0  40 53                           push rbx
0089A3F2  48 83 EC 60                     sub rsp, 0x60
0089A3F6  0F B6 41 1A                     movzx eax, byte ptr [rcx + 0x1a]
0089A3FA  48 8B D9                        mov rbx, rcx
0089A3FD  A8 02                           test al, 2
0089A3FF  74 35                           je 0x14089a436
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpDeleteNameCheck(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (96);
}
```

## 5. (Beta) C Style

```c
int64_t ObpDeleteNameCheck(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (96);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0089A3F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0089A3F0[BB_0089A3F0]
```
