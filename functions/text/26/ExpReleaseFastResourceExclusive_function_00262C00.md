# ExpReleaseFastResourceExclusive

- RVA: `0x00262C00`–`0x00262C17` (길이 `23` bytes)
- VA: `0x0000000140262C00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064588`
- 디코드: `6`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExReleaseFastResourceShared](../4F/ExReleaseFastResourceShared_function_004F59C0.md) at `0x004F5AF4`
- [ExReleaseFastResourceExclusive](../65/ExReleaseFastResourceExclusive_function_006588F0.md) at `0x00658A18`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00262C11` → [sub_00262C98](Unknown_function_00262C98.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00262C00  40 53                           push rbx
00262C02  48 83 EC 20                     sub rsp, 0x20
00262C06  83 69 60 01                     sub dword ptr [rcx + 0x60], 1
00262C0A  48 8D 41 40                     lea rax, [rcx + 0x40]
00262C0E  48 8B D9                        mov rbx, rcx
00262C11  0F 85 81 00 00 00               jne 0x140262c98
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpReleaseFastResourceExclusive(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
int64_t ExpReleaseFastResourceExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00262C00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00262C00[BB_00262C00]
```
