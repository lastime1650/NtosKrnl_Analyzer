# MiDispatchFault

- RVA: `0x00320520`–`0x00320540` (길이 `32` bytes)
- VA: `0x0000000140320520`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075638`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_0027F063](../27/Unknown_function_0027F063.md) at `0x0027F0A1`
- [MiInPagePageTable](../3E/MiInPagePageTable_function_003EF8DC.md) at `0x003EFBD8`

### Static image references
- `0x00320532` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00320520  4C 8B DC                        mov r11, rsp
00320523  55                              push rbp
00320524  53                              push rbx
00320525  41 56                           push r14
00320527  49 8D 6B 98                     lea rbp, [r11 - 0x68]
0032052B  48 81 EC 50 01 00 00            sub rsp, 0x150
00320532  48 8B 05 07 A2 AE 00            mov rax, qword ptr [rip + 0xaea207]
00320539  48 33 C4                        xor rax, rsp
0032053C  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDispatchFault(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 11444743)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 104 + 32) = result;
    return result;
}
```

## 5. (Beta) C Style

```c
void MiDispatchFault(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0xAEA207)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x68 + 0x20) = result;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00320520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00320520[BB_00320520]
```
