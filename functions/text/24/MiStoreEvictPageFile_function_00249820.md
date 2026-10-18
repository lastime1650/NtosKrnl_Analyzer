# MiStoreEvictPageFile

- RVA: `0x00249820`–`0x00249850` (길이 `48` bytes)
- VA: `0x0000000140249820`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000628DC`
- 디코드: `12`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiStoreEvictThread](../3A/MiStoreEvictThread_function_003A42D0.md) at `0x003A44FB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0024984A` → [sub_00249B5F](Unknown_function_00249B5F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00249820  4C 8B DC                        mov r11, rsp
00249823  41 55                           push r13
00249825  48 81 EC 80 00 00 00            sub rsp, 0x80
0024982C  33 C0                           xor eax, eax
0024982E  0F 57 C0                        xorps xmm0, xmm0
00249831  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00249836  4C 8B E9                        mov r13, rcx
00249839  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0024983E  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
00249842  8B 81 A8 00 00 00               mov eax, dword ptr [rcx + 0xa8]
00249848  85 C0                           test eax, eax
0024984A  0F 84 0F 03 00 00               je 0x140249b5f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiStoreEvictPageFile(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;

    v_rsp = (v_rsp) - (128);
    result = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 72) = 0;
}
```

## 5. (Beta) C Style

```c
int64_t MiStoreEvictPageFile(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;

    local_rsp = (local_rsp) - (128);
    result = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x48) = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xA8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00249820&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00249820[BB_00249820]
```
